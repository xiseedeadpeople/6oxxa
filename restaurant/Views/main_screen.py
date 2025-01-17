import flet as ft
from flet_core import LinearGradient

# •	Регистрация и управление клиентами, оформление туров.

# TODO:
#  https://habr.com/ru/articles/237931/                                -       DPI, screen resolution
#  https://danilin.biz/ios-device-display-resolution-reference         -       logic iphone screen resolution

def mainscreen(page: ft.Page):
    def youchangechoice(e):
        """ функция, которая отвечает за выбранный таб """
        youindex = e.control.selected_index

        if youindex == 0:
            page.go('/user_mainscreen/main_tab')

        if youindex == 1:
            page.go('/user_mainscreen/closest_flights')

        if youindex == 2:
            page.go('/user_mainscreen/my_orders')

        if youindex == 3:
            page.go('/user_mainscreen/notifications')


        page.update()

    mytab = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        unselected_label_color='black',
        label_color='white',
        indicator_color='white',
        indicator_border_radius=30,
        divider_color='black',
        divider_height=0,
        scrollable=True,
        on_change=youchangechoice,

        tabs=[
            ft.Tab(text='Главная', icon='Home'), # бронируем
            ft.Tab(text='История заказов', icon=ft.Icons.HISTORY_TOGGLE_OFF_ROUNDED), # бронируем
            ft.Tab(text='Меню', icon=ft.Icons.RESTAURANT_MENU_ROUNDED), # бронируем
            ft.Tab(text='Оборудование', icon=ft.Icons.ADF_SCANNER_ROUNDED), # уведомления о рейсах
            ft.Tab(text='Персонал', icon=ft.Icons.PEOPLE_ALT_ROUNDED) # уведомления о рейсах
        ]
    )

    mybar = ft.Container(
        gradient=LinearGradient(begin=ft.alignment.top_left,
                                end=ft.alignment.bottom_right,
                                colors=['#fc4795', '#7c69f0']),

        border_radius=ft.border_radius.vertical(bottom=30),
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=10, color='#fc4795'),
        width=page.window.width,
        height=150,
        padding=10,

        content=ft.Column([
            ft.Row([ft.IconButton(icon='menu', icon_size=25, icon_color='white'),
                    ft.Text(value='Flyin', size=25, color='white', weight=ft.FontWeight.BOLD),
                    ft.IconButton(icon='notifications', icon_size=25, icon_color='white'),
                    ft.IconButton(icon='search', icon_size=25, icon_color='white')]
                   ),
            mytab],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    )

    # -------------------------------------------------------------------------------


    page.overlay.append(mybar)
    return ft.View(
        route='/user_mainscreen',
        bgcolor='white',
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[ft.Text('main_tab', color='black', size=30)],
    )
