import flet as ft
from datetime import datetime, timezone
from db import get_db, Reservation, HistoryReservation
from prefs.colors import colors, style, error_style

today = datetime.today().date().strftime('%d.%m.%Y')

def reservation(page):
    db = next(get_db())

    def handle_dlg_action_clicked(e):
        page.close(dlg)
        dlg.data.confirm_dismiss(e.control.data)

    dlg = ft.CupertinoAlertDialog(
        modal=True,
        title=ft.Text('Пожалуйста, подтвердите', style=style(size=13, color='white')),
        content=ft.Text('Вы действительно хотите закрыть бронь?', style=style(size=13, color='white')),
        actions=[
            ft.Container(ft.Text('Да', style=error_style(size=13)), data=True, on_click=handle_dlg_action_clicked,
                         alignment=ft.alignment.center, width=50, height=50),
            ft.Container(ft.Text('Нет', style=style(size=13)), data=False, on_click=handle_dlg_action_clicked,
                         alignment=ft.alignment.center),
        ]
    )

    def refresh_list_view():
        lww.controls.clear()
        active_reservations = db.query(Reservation).filter(Reservation.completed == False).all()

        for rreservation in active_reservations:
            lww.controls.append(ft.Dismissible(
                content=ft.Container(
                    content=ft.Text(rreservation.description, style=style(size=18)),
                    alignment=ft.alignment.center,
                    bgcolor=colors['bg'],
                    padding=10,
                    height=100,
                    border_radius=ft.border_radius.all(10)
                ),
                dismiss_direction=ft.DismissDirection.END_TO_START,
                background=ft.Container(bgcolor=colors['primary']),
                secondary_background=ft.Container(bgcolor=colors['primary']),
                on_dismiss=handle_dismiss,
                on_confirm_dismiss=handle_confirm_dismiss,
                dismiss_thresholds={ft.DismissDirection.END_TO_START: 0.2},
                data=rreservation.id
            ))
        page.update()

    def handle_confirm_dismiss(e: ft.DismissibleDismissEvent):

        if e.direction == ft.DismissDirection.START_TO_END:
            reservation_id = e.control.data
            completed_reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
            if completed_reservation:
                completed_reservation.completed = True
                db.commit()
                refresh_list_view()
                show_snackbar(f'Бронь {completed_reservation.description} завершена', sstyle=style(size=15))
        elif e.direction == ft.DismissDirection.END_TO_START:
            dlg.data = e.control
            page.open(dlg)

    def handle_dismiss(e):

        reservation_id = e.control.data
        completed_reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
        if completed_reservation:

            history_reservation = HistoryReservation(description=completed_reservation.description,
                                                     date=datetime.now(timezone.utc))
            db.add(history_reservation)
            db.delete(completed_reservation)
            db.commit()

        e.control.parent.controls.remove(e.control)
        page.update()

    def handle_add(e):
        new_reservation = f"Бронь {today} - {len(db.query(Reservation).all()) + 1}"
        db.add(Reservation(description=new_reservation, completed=False))
        db.commit()
        refresh_list_view()
        show_snackbar(f'Бронь {today} - {len(db.query(Reservation).all())} добавлена', sstyle=style(size=15))

    def show_snackbar(message, sstyle=error_style(size=15)):

        snackbar = ft.SnackBar(
            ft.Container(ft.Text(message, style=sstyle), alignment=ft.alignment.center),
            open=True, bgcolor=colors['bg'], duration=1000
        )
        page.overlay.append(snackbar)
        page.update()

    add_employee_btn = ft.IconButton(
        icon=ft.Icons.ADD,
        on_click=handle_add,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=30),
            bgcolor=colors['primary'],
            color='black',
        ),
        width=60,
        height=60,
    )

    lww = ft.ListView(
        expand=True,
        controls=[],
        spacing=10,
        width=360,
        first_item_prototype=True,
        height=635,
    )


    refresh_list_view()

    return ft.View(
        route='/user_mainscreen',
        bgcolor=colors['bg'],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Container(height=150, opacity=0),
            ft.Stack(
                controls=[
                    lww,
                    ft.Container(add_employee_btn, padding=ft.padding.only(right=20, bottom=30))
                ],
                alignment=ft.alignment.bottom_right
            ),
            ft.Container(height=10)
        ],
    )
