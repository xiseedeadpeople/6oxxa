import flet as ft
from db import get_db, HistoryReservation
from prefs.colors import colors, style, error_style


def orders_history(page):
    db = next(get_db())

    def refresh_list_view():
        lww.controls.clear()

        reservation_list = db.query(HistoryReservation).order_by(HistoryReservation.date.desc()).all()

        for reservation in reservation_list:
            lww.controls.append(ft.Container(
                content=ft.Text(reservation.description, style=style(size=18)),
                alignment=ft.alignment.center,
                bgcolor=colors['bg'],
                padding=10,
                height=100,
                border_radius=ft.border_radius.all(10)
            ))

        page.update()

    lww = ft.ListView(
        expand=True,
        controls=[],
        spacing=10,
        width=360,
        first_item_prototype=True,
        height=635,
    )

    refresh_list_view()

    def handle_add(e):
        db.query(HistoryReservation).delete()
        db.commit()
        refresh_list_view()
        page.close(delete_history_dlg)

    def handle_dissmiss(e):
        page.close(delete_history_dlg)

    delete_history_dlg = ft.CupertinoAlertDialog(
        modal=True,
        title=ft.Text('Пожалуйста, подтвердите', style=style(size=13, color='white')),
        content=ft.Text('Вы действительно хотите удалить все?', style=style(size=13, color='white')),
        actions=[
            ft.Container(ft.Text('Да', style=error_style(size=13)), data=True, on_click=handle_add,
                         alignment=ft.alignment.center, width=50, height=50),
            ft.Container(ft.Text('Нет', style=style(size=13)), data=False, on_click=handle_dissmiss,
                         alignment=ft.alignment.center),
        ]
    )


    delete_history_btn = ft.IconButton(
        icon=ft.Icons.DELETE,
        on_click=lambda e: page.open(delete_history_dlg),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=30),
            bgcolor=colors['primary'],
            color='black',
        ),
        width=60,
        height=60,
    )

    return ft.View(
        route='/user_mainscreen',
        bgcolor=colors['bg'],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Container(height=150),
            ft.Stack(
                controls=[
                    lww,
                    ft.Container(delete_history_btn, padding=ft.padding.only(right=20, bottom=30))
                ],
                alignment=ft.alignment.bottom_right
            ),
            ft.Container(height=10)
        ],
    )
