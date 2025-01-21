import flet as ft
from flet_core import LinearGradient



def main(page: ft.Page):
    page.window.width = 390
    page.window.height = 844
    page.window.always_on_top = True
    page.window.maximizable = False
    page.window.resizable = False
    page.bgcolor = '#000000'
    page.horizontal_alignment = 'center'
    page.padding = 10
    page.spacing = 0

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def youchangechoice(e):

        """ функция, которая отвечает за выбранный таб """
        youindex = e.control.selected_index

        if youindex == 0:
            # page.go('/.../main_tab')

            pass

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
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    lw = ft.ListView(
        controls=[
            ft.Container(ft.Text('1', size=40, color='white'), width=200, height=150, bgcolor='#202020', alignment=ft.alignment.center),
            ft.Container(ft.Text('2', size=40, color='white'), width=200, height=150, bgcolor='#202020', alignment=ft.alignment.center),
            ft.Container(ft.Text('3', size=40, color='white'), width=200, height=150, bgcolor='#202020', alignment=ft.alignment.center),
            ft.Container(ft.Text('4', size=40, color='white'), width=200, height=150, bgcolor='#202020', alignment=ft.alignment.center),
            ft.Container(ft.Text('5', size=40, color='white'), width=200, height=150, bgcolor='#202020', alignment=ft.alignment.center),
            ft.Container(ft.Text('6', size=40, color='white'), width=200, height=150, bgcolor='#202020', alignment=ft.alignment.center),
            ft.Container(ft.Text('7', size=40, color='white'), width=200, height=150, bgcolor='#202020', alignment=ft.alignment.center),
            ft.Container(ft.Text('8', size=40, color='white'), width=200, height=150, bgcolor='#202020', alignment=ft.alignment.center),
            ft.Container(ft.Text('9', size=40, color='white'), width=200, height=150, bgcolor='#202020', alignment=ft.alignment.center),
            ft.Container(ft.Text('10', size=40, color='white'), width=200, height=150, bgcolor='#202020', alignment=ft.alignment.center),
            ft.Container(ft.Text('11', size=40, color='white'), width=200, height=150, bgcolor='#202020', alignment=ft.alignment.center),
        ],
        spacing=10,
        width=360,
        first_item_prototype=True,

        # item_extent=150,
        height=635,
    )
    page.overlay.append(mybar)
    page.add(ft.Container(height=150), lw)


ft.app(main)
