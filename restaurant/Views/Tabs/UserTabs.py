import flet as ft

def main_tab(page: ft.Page):
    return ft.View(
        route='/user_mainscreen',
        bgcolor='white',
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[ft.Text('main_tab', color='black', size=30)],
    )


def closest_flights(page: ft.Page):
    return ft.View(
        route='/user_mainscreen',
        bgcolor='white',
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[ft.Text('closest_flights', color='black', size=30)],
    )

def my_orders(page: ft.Page):
    return ft.View(
        route='/user_mainscreen',
        bgcolor='white',
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[ft.Text('my_orders', color='black', size=30)],
    )

def notifications(page: ft.Page):
    return ft.View(
        route='/user_mainscreen',
        bgcolor='white',
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[ft.Text('notifications', color='black', size=30)],
    )
