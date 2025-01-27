import flet as ft
import datetime


def staff(page: ft.Page):
    return ft.View(
        route='/user_mainscreen',
        bgcolor='#000000',
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[ft.Text('staff', color='black', size=30)],
    )
