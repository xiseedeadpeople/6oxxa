import flet as ft
from prefs.colors import colors, style
from views.tabs.staff import staff


def main_screen(page: ft.Page):

    def youchangechoice(e):
        youindex = e.control.selected_index

        if youindex == 0:
            page.go('/user_mainscreen/staff')

        if youindex == 1:
            page.go('/user_mainscreen/equipment')

        if youindex == 2:
            page.go('/user_mainscreen/reservation')

        if youindex == 3:
            page.go('/user_mainscreen/orders_history')

        page.update()

    mytab = ft.Tabs(
        selected_index=0,
        animation_duration=600,
        unselected_label_color=colors['secondary'],
        label_color=colors['primary'],
        indicator_color=colors['primary'],
        indicator_border_radius=30,
        divider_height=0,
        scrollable=True,
        on_change=youchangechoice,

        tabs=[
            ft.Tab(text='Персонал', icon=ft.icons.PEOPLE_ALT_ROUNDED),  # уведомления о рейсах
            ft.Tab(text='Оборудование', icon=ft.icons.ADF_SCANNER_ROUNDED),  # уведомления о рейсах
            ft.Tab(text='Брони', icon=ft.icons.RESTAURANT),  # бронируем
            ft.Tab(text='История заказов', icon=ft.icons.HISTORY_TOGGLE_OFF_ROUNDED),  # бронируем
        ]
    )

    dlg = ft.AlertDialog(barrier_color=ft.Colors.with_opacity(0.96, 'black'),
                         title=ft.Text('мысли о смерти не сделали меня самураем', style=style(size=25)),
                         content=ft.Text('github.com/xiseedeadpeople/6oxxa', style=style(size=15)),
                         bgcolor=ft.Colors.with_opacity(0, '#080808'))


    mybar = ft.Container(
        bgcolor=colors['bg'],
        border_radius=ft.border_radius.vertical(bottom=30),
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=100, color=colors['block_shadow']),
        width=page.window.width,
        height=150,
        padding=10,

        content=ft.Column([
            ft.Row([ft.IconButton(icon=ft.Icons.CODE, icon_size=25, icon_color=colors['primary'],
                                  on_click=lambda e: page.open(dlg)),

                    ft.Text('солидный рестик✦₊ﾟ',
                            style=style(color=colors['primary'],
                            shadowclr=colors['font_shadow'], size=20))]),
            mytab],

            alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    )

    page.overlay.append(mybar)
    return staff(page)
