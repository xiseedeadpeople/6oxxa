import flet as ft
from datetime import datetime
from flight.prefs.colors import colors, style
from flight.models import Session, Flight

def ordrs_history(page: ft.Page):
    session = Session()
    past_flights = session.query(Flight).filter(Flight.departure_date < datetime.now()).all()
    session.close()

    flight_texts = []
    for flight in past_flights:
        flight_texts.append(ft.Text(f"От: {flight.from_city}, Куда: {flight.to_city}, Дата: {flight.departure_date.strftime('%d/%m/%Y')}", style=style()))

    return ft.View(
        route='/user_mainscreen',
        bgcolor=colors['bg'],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=flight_texts or [ft.Text('Нет завершенных рейсов', style=style())],
    )
