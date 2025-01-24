import flet as ft
import datetime


def reservation(page: ft.Page):

    lw = ft.ListView(
        controls=[
            ft.Container(ft.Text('1', size=40, color='white'), width=200, height=150,
                         bgcolor='#202020', alignment=ft.alignment.center, border_radius=20),

            ft.Container(ft.Text('2', size=40, color='white'), width=200, height=150,
                         bgcolor='#202020', alignment=ft.alignment.center, border_radius=20),

            ft.Container(ft.Text('3', size=40, color='white'), width=200, height=150,
                         bgcolor='#202020', alignment=ft.alignment.center, border_radius=20),

            ft.Container(ft.Text('4', size=40, color='white'), width=200, height=150,
                         bgcolor='#202020', alignment=ft.alignment.center, border_radius=20),

            ft.Container(ft.Text('5', size=40, color='white'), width=200, height=150,
                         bgcolor='#202020', alignment=ft.alignment.center, border_radius=20),

            ft.Container(ft.Text('6', size=40, color='white'), width=200, height=150,
                         bgcolor='#202020', alignment=ft.alignment.center, border_radius=20),

            ft.Container(ft.Text('7', size=40, color='white'), width=200, height=150,
                         bgcolor='#202020', alignment=ft.alignment.center, border_radius=20),

            ft.Container(ft.Text('8', size=40, color='white'), width=200, height=150,
                         bgcolor='#202020', alignment=ft.alignment.center, border_radius=20),

            ft.Container(ft.Text('9', size=40, color='white'), width=200, height=150,
                         bgcolor='#202020', alignment=ft.alignment.center, border_radius=20),

            ft.Container(ft.Text('10', size=40, color='white'), width=200, height=150,
                         bgcolor='#202020', alignment=ft.alignment.center, border_radius=20),

            ft.Container(ft.Text('99999', size=40, color='white'), width=200, height=150,
                         bgcolor='#202020', alignment=ft.alignment.center, border_radius=20),

        ],
        spacing=10,
        width=360,
        first_item_prototype=True,

        # item_extent=150,
        height=635,
    )

    return ft.View(
        route='/user_mainscreen',
        bgcolor='#000000',
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[ft.Container(height=150), lw],
    )
