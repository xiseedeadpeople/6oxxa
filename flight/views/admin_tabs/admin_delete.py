import flet as ft
from prefs.stylesnhelpers import colors, style, show_snackbar
from models import Session, Flight

def admin_delete(page: ft.Page):
    session = Session()
    flight_id_input = ft.TextField(label="ID рейса для удаления")
    flights_list_view = ft.ListView(expand=True, spacing=10, width=360, first_item_prototype=True, height=635)

    def delete_flight(e):
        flight_id = flight_id_input.value

        if flight_id:
            flight = session.query(Flight).filter(Flight.id == flight_id).first()
            if flight:
                session.delete(flight)
                session.commit()
                show_snackbar(page, f'Рейс {flight_id} удален.', textsize=25)
                page.update()
            else:
                show_snackbar(page, message=f'Рейс {flight_id} не найден.', textcolor='red', textsize=25)
        else:
            show_snackbar(page, 'Введите ID рейса', textsize=25)

    delete_button = ft.ElevatedButton("Удалить рейс", on_click=delete_flight)

    def display_flights():
        flights_list_view.controls.clear()
        flights = session.query(Flight).order_by(Flight.id.desc()).all() # .limit(int)
        if not flights:
            flights_list_view.controls.append(ft.Text("Нет доступных рейсов."))
        else:
            for flight in flights:
                flights_list_view.controls.append(ft.Container(
                    content=ft.Column([
                        ft.Text(f"ID: {flight.id}", style=style(size=17)),
                        ft.Text(f"{flight.from_city} - {flight.to_city}", style=style(size=17)),
                        ft.Text(f"{flight.departure_date} - {flight.return_date}", style=style(size=17)),
                    ]),
                    padding=20,
                    bgcolor=colors['bg'],
                    border_radius=8,
                    border=ft.border.all(width=1, color=colors['secondary'])
                ))

    display_flights()

    return ft.View(
        route='/admin_mainscreen',
        bgcolor=colors['bg'],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Column(
                controls=[
                    ft.Container(height=180, bgcolor=colors['bg']),
                    flight_id_input,
                    delete_button,
                ],
            ),
            flights_list_view
        ],

    )
