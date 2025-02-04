import flet as ft
import threading

class ContextMenuItem:
    DEFAULT_ACTIONS = [
        {
            'text': "Выдать премию",
            'is_default': True,
            'trailing_icon': ft.icons.ATTACH_MONEY,
            'callback': None,  # Установим как None, позже обновим
        },
        {
            'text': "Выдать штраф",
            'is_default': True,
            'trailing_icon': ft.icons.MONEY_OFF,
            'callback': None,  # Установим как None, позже обновим
        },
        {
            'text': "Повысить",
            'trailing_icon': ft.icons.WORKSPACE_PREMIUM,
            'callback': None,  # Установим как None, позже обновим
        },
        {
            'text': "Уволить",
            'is_destructive': True,
            'trailing_icon': ft.icons.INDETERMINATE_CHECK_BOX,
            'callback': None,
        },
    ]

    def __init__(self, title, actions=None, index=None, lw=None, remove_callback=None, page=None):
        self.title = title
        self.actions = actions if actions is not None else self.DEFAULT_ACTIONS
        self.index = index
        self.lw = lw
        self.remove_callback = remove_callback
        self.page = page  # Сохраняем ссылку на страницу

        # Устанавливаем колбэки для действий
        self.actions[0]['callback'] = self.create_award_callback()
        self.actions[1]['callback'] = self.create_fine_callback()
        self.actions[2]['callback'] = self.create_promote_callback()

        if self.remove_callback is not None:
            self.actions[-1]['callback'] = self.create_remove_callback()

    def create_award_callback(self):
        def award_employee(e):
            new_snack_bar = ft.SnackBar(ft.Text('Сотрудник получил премию (1000₽)'),
                                        open=True, bgcolor='#4caf50', duration=1000)
            self.page.overlay.append(new_snack_bar)
            self.page.update()

        return award_employee

    def create_fine_callback(self):
        def fine_employee(e):
            new_snack_bar = ft.SnackBar(ft.Text('Сотрудник получил штраф.'),
                                        open=True, bgcolor='#f44336', duration=1000)
            self.page.overlay.append(new_snack_bar)
            self.page.update()
        return fine_employee

    def create_promote_callback(self):
        def promote_employee(e):
            new_snack_bar = ft.SnackBar(ft.Text('Сотрудник повышен.'),
                                        open=True, bgcolor='#2196F3', duration=1000)
            self.page.overlay.append(new_snack_bar)
            self.page.update()
        return promote_employee

    def create_remove_callback(self):
        def remove_employee(e):
            if self.remove_callback is not None:
                self.remove_callback(self.index)
        return remove_employee

    def create(self):
        return ft.CupertinoContextMenu(
            enable_haptic_feedback=True,
            content=ft.Container(
                ft.TextButton(text=self.title),
                width=200,
                height=150,
                bgcolor='#f2f3fa',
                alignment=ft.alignment.center,
                border_radius=20,
                padding=10,
            ),
            actions=self.create_actions()
        )

    def create_actions(self):
        action_items = []
        for action in self.actions:
            action_items.append(
                ft.CupertinoContextMenuAction(
                    text=action['text'],
                    is_default_action=action.get('is_default', False),
                    is_destructive_action=action.get('is_destructive', False),
                    trailing_icon=action.get('trailing_icon', ft.icons.MORE),
                    on_click=action['callback']
                )
            )
        return action_items


def staff(page):
    staff_list = [f'Сотрудник {i}' for i in range(1, 13)]  # Полный список сотрудников

    lw = ft.ListView(spacing=10, width=360, first_item_prototype=True, height=635)

    def refresh_list_view():
        lw.controls.clear()  # Очистим текущие элементы
        for i, employee in enumerate(staff_list):
            item = ContextMenuItem(title=employee, index=i, lw=lw, remove_callback=remove_employee, page=page).create()
            lw.controls.append(item)  # Добавляем новые элементы
        page.update()  # Обновляем страницу после обновления списка

    def remove_employee(index):
        def close_snack_bar(snack_bar):
            snack_bar.open = False
            page.update()

        new_snack_bar = ft.SnackBar(ft.Text('Сотрудник удален'),
                                    open=True, bgcolor='#36618e', duration=1000)
        page.overlay.append(new_snack_bar)
        page.update()

        staff_list.pop(index)
        refresh_list_view()

    page.window.width = 390
    page.window.height = 844
    page.window.always_on_top = True
    page.window.maximizable = False
    page.window.resizable = False
    page.padding = 0
    page.spacing = 0
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Добавляем View на страницу
    view = ft.View(
        route='/user_mainscreen',
        bgcolor='#000000',
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[ft.Container(height=150, opacity=0), lw],
    )

    page.views.append(view)
    refresh_list_view()

    return view
