from prefs.colors import colors, style, error_style
from prefs.fonts.font_setup import font_list
import flet as ft


def login_screen(page: ft.Page):
    page.fonts = font_list

    def password_focus(e):
        password.error_text = ''
        page.update()

    def password_blur(e):
        if len(password.value) == 0:
            password.error_text = 'Введите пароль'
        page.update()

    def phone_focus(e):
        phone.prefix_style = style(color='black')
        phone.error_text = ''
        page.update()

    def phone_blur(e):
        phone.prefix_style = style()
        if len(phone.value) == 0:
            phone.error_text = 'Введите номер'

        elif 1 <= len(phone.value) < 14:
            phone.error_text = 'Неверный формат номера'
        page.update()

    def format_phone(e):
        phone.error_text = ''
        new_value = (phone.value.replace(" ", "").replace("(", "")
                     .replace(")", "").replace("-", ""))  # Убираем все ненужные символы

        # # # Ограничиваем длину введенной строки
        if len(phone.value) > 9:
            phone.value = new_value[:11]
            formatted_value = f'({phone.value[:3]}) {new_value[3:6]}-{new_value[6:8]}-{new_value[8:10]}'
            phone.value = formatted_value
            password.focus()
            phone.update()

    dlg = ft.AlertDialog(barrier_color=ft.Colors.with_opacity(0.96, 'black'),
                         title=ft.Text('password: 123', style=style(size=25)),
                         bgcolor=ft.Colors.with_opacity(0, '#080808'))

    passforgot_btn = ft.CupertinoButton(
        content=ft.Container(ft.Text('Забыли пароль?',
                                     style=style(color=colors['inv_primarytext'],
                                                 shadowclr=colors['inv_fontshadow'], spreadshadow=100)),
        on_click=lambda e: page.open(dlg)))

    phone = ft.TextField(
        cursor_color = 'black',
        focused_color='black',
        label='Номер телефона',
        width=300,
        border_radius=10,
        prefix_text='+7 ',
        label_style=style(),
        text_style=style(),
        prefix_style=style(color='black'),
        error_style=error_style(size=15),
        adaptive=True,
        border=ft.InputBorder.NONE,
        fill_color=colors['bg'],
        input_filter=ft.NumbersOnlyInputFilter(),
        on_change=format_phone,
        on_blur=phone_blur, on_focus=phone_focus
    )

    password = ft.TextField(
        cursor_color='black',
        focused_color = 'black',
        label='Пароль',
        width=300,
        border_radius=10,
        password=True,
        can_reveal_password=True,
        label_style=style(),
        text_style=style(),
        prefix_style=style(),
        error_style=error_style(size=15),
        on_focus=password_focus, on_blur=password_blur,
        border=ft.InputBorder.NONE, fill_color=colors['bg'], adaptive=True,
    )

    mybarx = ft.Container(
        bgcolor=colors['bg'],
        border_radius=ft.border_radius.vertical(bottom=30),
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=100, color=colors['block_shadow']),
        width=page.window.width, height=150, alignment=ft.alignment.center,
        content=ft.Container(ft.Text('6oxxa restaurant✦₊ﾟ', style=style(color=colors['primary'],
                                                            shadowclr=colors['font_shadow'], size=20)))
    )


    def go_to_welcome(e):

        if len(phone.value) == 0:
            phone.error_text = 'Введите номер'
            phone.update()

        elif len(phone.value) != 15:
            phone.error_text = 'Неверный формат номера'
            phone.update()

        if len(password.value) == 0:
            password.error_text = 'Введите пароль'
            password.update()

        elif password.value != '123':
            password.error_text = 'Неверный пароль!'
            password.update()

        elif password.value == '123' and len(phone.value) == 15:
            page.go("/user_mainscreen")

    btn = ft.Container(
        ft.Text('Войти', style=style()),
        width=300, height=50, on_click=go_to_welcome, border_radius=20, alignment=ft.alignment.center,
        shadow=ft.BoxShadow(spread_radius=0.5, blur_radius=50, color=colors['block_shadow']),
        bgcolor=colors['bg'])


    main_container = ft.Column(
        controls=[
            mybarx,
            ft.Container(height=150),
            ft.Column(controls=[phone, ft.Column([password, passforgot_btn],
                                spacing=0, horizontal_alignment=ft.CrossAxisAlignment.END),btn],

                      spacing=30, alignment=ft.alignment.center)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    return ft.View(
            "/",
            [main_container], bgcolor=colors['bg'], padding=0)
