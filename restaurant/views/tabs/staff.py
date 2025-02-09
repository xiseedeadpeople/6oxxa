import flet as ft
from prefs.colors import colors, style, error_style
from db import get_db, Staff
import re

class ContextMenuItem:
    def __init__(self, title, index, remove_callback, page):
        self.title = title
        self.index = index
        self.remove_callback = remove_callback
        self.page = page

    def show_snackbar(self, message, sstyle=style(size=15, color=colors['primary'])):
        snackbar = ft.SnackBar(
            ft.Container(ft.Text(message, style=sstyle), alignment=ft.alignment.center),
            open=True, bgcolor=colors['bg'], duration=1000
        )
        self.page.overlay.append(snackbar)
        self.page.update()

    def generate_actions(self):
        return [
            ft.CupertinoContextMenuAction(
                text='Выдать премию',
                is_default_action=True,
                trailing_icon=ft.icons.ATTACH_MONEY,
                on_click=lambda e: self.show_snackbar('Выдана премия (1000₽)')
            ),
            ft.CupertinoContextMenuAction(
                text='Повысить',
                trailing_icon=ft.icons.WORKSPACE_PREMIUM,
                on_click=lambda e: self.show_snackbar('Сотрудник повышен.')
            ),
            ft.CupertinoContextMenuAction(
                text='Выдать штраф',
                trailing_icon=ft.icons.MONEY_OFF,
                on_click=lambda e: self.show_snackbar('Выдан штраф (1000₽)', sstyle=error_style(size=15))
            ),
            ft.CupertinoContextMenuAction(
                text='Уволить',
                is_destructive_action=True,
                trailing_icon=ft.icons.INDETERMINATE_CHECK_BOX,
                on_click=lambda e: self.remove_callback(self.index)
            ),
        ]

    def create(self):
        return ft.CupertinoContextMenu(
            enable_haptic_feedback=True,
            content=ft.Container(
                ft.Text(self.title, style=style(size=15)),
                width=250,
                height=150,
                bgcolor=colors['bg'],
                shadow=ft.BoxShadow(spread_radius=1, blur_radius=5, color=colors['block_shadow']),
                alignment=ft.alignment.center,
                border_radius=20,
                padding=10,
            ),
            actions=self.generate_actions()
        )

def staff(page):

    db = next(get_db())
    staff_list = db.query(Staff).all()
    lw = ft.ListView(spacing=10, width=360, height=635)

    def tf_focus(e):
        e.control.error_text = ''
        employee_dialog.update()

    def tf_blur(e):
        if len(e.control.value.strip()) == 0:
            e.control.error_text = 'Поле не должно быть пустым!'
        elif 'Abc/Абв/-' in e.control.value:
            e.control.value = ''
        employee_dialog.update()

    def textfield(purpose: str):
        return ft.TextField(
            cursor_color = 'black',
            focused_color='black',
            label=purpose,
            width=300,
            border_radius=10,
            label_style=style(),
            text_style=style(),
            error_style=error_style(size=10),
            adaptive=True,
            border=ft.InputBorder.NONE,
            fill_color=colors['bg'],
            on_blur=tf_blur,
            on_focus=tf_focus,
            on_change=on_text_change
        )

    def refresh_list_view():
        sstaff_list = db.query(Staff).all()
        lw.controls.clear()
        for i, employee in enumerate(sstaff_list):
            item = ContextMenuItem(f'{employee.last_name} ϟ {employee.position}', i, remove_employee, page).create()
            lw.controls.append(item)
        page.update()

    def remove_employee(index):

        refresh_list_view()

        staff_list = db.query(Staff).all()

        if index < len(staff_list):
            employee = staff_list[index]
            db.delete(employee)
            db.commit()

            # Refresh the ListView after deleting
            refresh_list_view()
            show_snackbar('Сотрудник уволен')
        else:
            show_snackbar('Ошибка: Сотрудник не найден', sstyle=error_style(size=15))

    def on_text_change(e):
        if bool(re.search(r'\d', e.control.value)):
            e.control.value = ''
        employee_dialog.update()

    def handle_add(e):
        if len(name.value) > 1:
            name.value = name.value.capitalize()
            if len(last_name.value) > 1:
                last_name.value = last_name.value.capitalize()
                if len(patronymic.value) > 1:
                    patronymic.value = patronymic.value.capitalize()
                    if len(work_position.value) > 1:
                        work_position.value = work_position.value.capitalize()

                        page.close(employee_dialog)
                        new_employee = Staff(first_name=name.value,
                                             last_name=last_name.value,
                                             position=work_position.value)

                        db.add(new_employee)
                        db.commit()
                        db.refresh(new_employee)

                        show_snackbar(f'Сотрудник {name.value} добавлен', sstyle=style(size=15))
                        name.value, last_name.value, patronymic.value, work_position.value = '', '', '', ''
                        refresh_list_view()

    def handle_dissmiss(e):
        page.close(employee_dialog)

    name = textfield('Имя')
    last_name = textfield('Фамилия')
    patronymic = textfield('Отчество')
    work_position = textfield('Должность')

    employee_dialog = ft.AlertDialog(
        modal=True,
        bgcolor=colors['bg'],
        title=ft.Text('Добавить сотрудника', style=style(size=15)),
        content=ft.Column([name, last_name, patronymic, work_position], height=250),
        actions=[
            ft.Container(ft.Text('Да', style=style(size=15)),
                         data=True, on_click=handle_add, alignment=ft.alignment.center, width=80, height=50),
            ft.Container(ft.Text('Нет', style=error_style(size=15)),
                         data=False, on_click=handle_dissmiss, alignment=ft.alignment.center, width=80, height=50),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    def show_snackbar(message, sstyle=error_style(size=15)):
        snackbar = ft.SnackBar(
            ft.Container(ft.Text(message, style=sstyle), alignment=ft.alignment.center),
            open=True, bgcolor=colors['bg'], duration=1000
        )
        page.overlay.append(snackbar)
        page.update()

    add_employee_btn = ft.IconButton(
        icon=ft.Icons.ADD,
        on_click=lambda e: page.open(employee_dialog),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=30),
            bgcolor=colors['primary'],
            color='black',
        ),
        width=60,
        height=60,
    )

    refresh_list_view()

    return ft.View(
        route='/user_mainscreen',
        bgcolor=colors['bg'],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Container(height=150, opacity=0),
            ft.Stack(
                controls=[
                    lw,
                    ft.Container(add_employee_btn, padding=ft.padding.only(right=20, bottom=30))
                ],
                alignment=ft.alignment.bottom_right
            )
        ],
    )
