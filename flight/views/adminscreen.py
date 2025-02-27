import flet as ft
from prefs.stylesnhelpers import colors, style
from views.admin_tabs.admin_create import admin_create


def admin_screen(page: ft.Page):
    def youchangechoice(e):
        youindex = e.control.selected_index

        if youindex == 0:
            page.go('/admin_mainscreen/admin_create')


        if youindex == 1:
            page.go('/admin_mainscreen/admin_delete')

        if youindex == 2:
            page.go('/admin_mainscreen/admin_update')

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
            ft.Tab(text='Создать рейс'),
            ft.Tab(text='Удалить рейс'),
            ft.Tab(text='Изменить рейс'),
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
    return admin_create(page)
