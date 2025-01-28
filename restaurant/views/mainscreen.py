import flet as ft
from flet_core import LinearGradient
from views.tabs.reservation import reservation

# •	Регистрация и управление клиентами, оформление туров.

# TODO:
#  https://habr.com/ru/articles/237931/                                -       DPI, screen resolution
#  https://danilin.biz/ios-device-display-resolution-reference         -       logic iphone screen resolution


def main_screen(page: ft.Page):
    def youchangechoice(e):
        """ функция, которая отвечает за выбранный таб """
        youindex = e.control.selected_index

        if youindex == 0:
            page.go('/user_mainscreen/reservation')

        if youindex == 1:
            page.go('/user_mainscreen/orders_history')

        if youindex == 2:
            page.go('/user_mainscreen/menu')

        if youindex == 3:
            page.go('/user_mainscreen/equipment')

        if youindex == 4:
            page.go('/user_mainscreen/staff')
        page.update()

    mytab = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        unselected_label_color='white',
        label_color='black',
        indicator_color='black',
        indicator_border_radius=30,
        divider_height=0,
        scrollable=True,
        on_change=youchangechoice,

        tabs=[
            ft.Tab(text='Главная', icon='Home'),  # бронируем
            ft.Tab(text='История заказов', icon=ft.icons.HISTORY_TOGGLE_OFF_ROUNDED),  # бронируем
            ft.Tab(text='Меню', icon=ft.icons.RESTAURANT_MENU_ROUNDED),  # бронируем
            ft.Tab(text='Оборудование', icon=ft.icons.ADF_SCANNER_ROUNDED),  # уведомления о рейсах
            ft.Tab(text='Персонал', icon=ft.icons.PEOPLE_ALT_ROUNDED)  # уведомления о рейсах
        ]
    )

    mybar = ft.Container(
        gradient=LinearGradient(begin=ft.alignment.top_left,
                                end=ft.alignment.bottom_right,
                                colors=['#2bff88', '#36618e']),

        border_radius=ft.border_radius.vertical(bottom=30),
        shadow=ft.BoxShadow(spread_radius=3, blur_radius=100, color='#2bff88'),
        width=page.window.width,
        height=150,
        padding=10,

        content=ft.Column([
            ft.Row([ft.IconButton(icon='menu', icon_size=25, icon_color='white'),
                    ft.Text(value='xcxzzc', size=25, color='white', weight=ft.FontWeight.BOLD),
                    ft.IconButton(icon='notifications', icon_size=25, icon_color='white'),
                    ft.IconButton(icon='search', icon_size=25, icon_color='white')]
                   ),
            mytab],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    )

    page.overlay.append(mybar)
    return reservation(page)
