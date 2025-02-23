import flet as ft
from prefs.colors import colors, style
from views.tabs.flight_book import flight_book


def main_screen(page: ft.Page):
    def youchangechoice(e):
        youindex = e.control.selected_index

        if youindex == 0:
            page.go('/user_mainscreen/flight_book')


        if youindex == 1:
            page.go('/user_mainscreen/closest_flights')

        if youindex == 2:
            page.go('/user_mainscreen/ordrs_history')

        page.update()

    mytab = ft.Tabs(
        tab_alignment=ft.TabAlignment.FILL,
        selected_index=0,
        animation_duration=300,
        unselected_label_color=colors['secondary'],
        label_color=colors['primary'],
        indicator_color=colors['primary'],
        indicator_border_radius=30,
        divider_height=0,
        scrollable=True,
        on_change=youchangechoice,

        tabs=[
            ft.Tab(text='Главная страница'),  # уведомления о рейсах
            ft.Tab(text='Мои билеты'),  # бронируем
            ft.Tab(text='История'),  # бронируем
        ]
    )

    def open_repo(e):
        page.launch_url('https://github.com/xiseedeadpeople/6oxxa/tree/main/flight')

    github = ft.Container(
        content=ft.Image(src="prefs/icons/github.ico"), on_click=open_repo, padding=10)

    mybar = ft.Container(
        bgcolor=colors['bg'],
        border_radius=ft.border_radius.vertical(bottom=30),
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=100, color=colors['block_shadow']),
        width=page.window.width,
        height=150,
        padding=10,

        content=ft.Column([
            ft.Row([github,
                    ft.Text('cvvmoney✦₊',
                            style=style(color=colors['primary'],
                                        shadowclr=colors['font_shadow'], size=20))]),
            mytab],

            alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    )

    page.overlay.append(mybar)
    return flight_book(page)
