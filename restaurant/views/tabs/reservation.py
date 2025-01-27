import flet as ft


class ContextMenuItem:
    DEFAULT_ACTIONS = [
        {
            'text': "Action 1",
            'is_default': True,
            'trailing_icon': ft.Icons.CHECK,
            'callback': lambda e: print("Action 1"),
        },
        {
            'text': "Action 2",
            'trailing_icon': ft.Icons.MORE,
            'callback': lambda e: print("Action 2"),
        },
        {
            'text': "Action 3",
            'is_destructive': True,
            'trailing_icon': ft.Icons.CANCEL,
            'callback': lambda e: print("Action 3"),
        },
    ]

    def __init__(self, title, actions=None):
        self.title = title  # Заголовок элемента
        self.actions = actions if actions is not None else self.DEFAULT_ACTIONS


    def create(self):
        return ft.CupertinoContextMenu(
            enable_haptic_feedback=True,
            content=ft.Container(
                ft.Text(self.title, size=40, color='white'),
                width=200,
                height=150,
                bgcolor='#202020',
                alignment=ft.alignment.center,
                border_radius=20
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
                    trailing_icon=action.get('trailing_icon', ft.Icons.MORE),
                    on_click=action['callback']
                )
            )
        return action_items


def reservation(page):
    page.window.width = 390
    page.window.height = 844
    page.window.always_on_top = True
    page.window.maximizable = False
    page.window.resizable = False
    page.padding = 0
    page.spacing = 0
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    itms = [ContextMenuItem(title=f'Item {i}').create() for i in range(1, 13)]

    custom_actions = [
        {
            'text': "Custom Action 1",
            'trailing_icon': ft.Icons.ADD,
            'callback': lambda e: print("Custom Action 1"),
        },
        {
            'text': "Custom Action 2",
            'is_destructive': True,
            'trailing_icon': ft.Icons.REMOVE,
            'callback': lambda e: print("Custom Action 2"),
        },
    ]

    lw = ft.ListView(
        controls=itms,

        spacing=10,
        width=360,
        first_item_prototype=True,
        height=635,
    )

    lw.controls.append(ft.Container(height=1))


    return ft.View(
        route='/user_mainscreen',
        bgcolor='#000000',
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[ft.Container(height=150), lw, ft.Container(height=10)],
    )
