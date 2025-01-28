import flet as ft
import datetime


def menu(page: ft.Page):
    return ft.View(
        route='/user_mainscreen',
        bgcolor='#FFFFFF',
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[ft.Text('menu', color='black', size=30)],
    )
