import flet as ft
import datetime
from prefs.colors import colors, style

def closest_flights(page: ft.Page):

    return ft.View(
        route='/user_mainscreen',
        bgcolor=colors['bg'],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[ft.Text('closest_flights', style=style())],
    )
