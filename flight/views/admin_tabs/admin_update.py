import flet as ft
import datetime
from prefs.stylesnhelpers import colors, style, error_style, cities, show_snackbar, tfield
from models import Session, Flight


def admin_update(page: ft.Page):

    from_suggestions_list = ft.Row()
    to_suggestions_list = ft.Row()


    flight_id_input = tfield('ID рейса')

    def fromf_changed(e):
        from_suggestions_list.controls.clear()
        typed_text = e.control.value.lower().strip()
        if typed_text:
            for city in cities:
                if typed_text in city.lower():
                    from_suggestions_list.controls.append(
                        ft.TextButton(
                            text=city,
                            on_click=lambda x, c=city: select_from_suggestion(c)
                        )
                    )
        page.update()

    def select_from_suggestion(city_name):
        fromf.value = city_name
        from_suggestions_list.controls.clear()
        page.update()

    def tof_changed(e):
        to_suggestions_list.controls.clear()
        typed_text = e.control.value.lower().strip()
        if typed_text:
            for city in cities:
                if typed_text in city.lower():
                    to_suggestions_list.controls.append(
                        ft.TextButton(
                            text=city,
                            on_click=lambda x, c=city: select_to_suggestion(c)
                        )
                    )
        page.update()

    def select_to_suggestion(city_name):
        tof.value = city_name
        to_suggestions_list.controls.clear()
        page.update()

    fromf = ft.TextField(
        cursor_color='black',
        focused_color='black',
        label='Точка вылета',
        width=300,
        border_radius=10,
        on_change=fromf_changed,
        label_style=style(),
        text_style=style(),
        error_style=error_style(size=18, shadowclr='white'),
        prefix_style=style(color='black'),
        adaptive=True,
        border=ft.InputBorder.NONE,
        fill_color=colors['bg']
    )

    tof = ft.TextField(
        cursor_color='black',
        focused_color='black',
        label='Пункт назначения',
        width=300,
        border_radius=10,
        label_style=style(),
        text_style=style(),
        error_style=error_style(size=18, shadowclr='white'),
        prefix_style=style(color='black'),
        adaptive=True,
        border=ft.InputBorder.NONE,
        fill_color=colors['bg'],
        on_change=tof_changed
    )

    today = datetime.datetime.today()
    departure_date = None
    return_date = None



    date_text = ft.Text(f'Вылет', style=style())
    return_date_text = ft.Text(f'Прилёт', style=style())

    def handle_change(e):
        nonlocal departure_date
        selected_date = e.control.value
        if selected_date:
            departure_date = selected_date.date()
            date_text.value = f'{departure_date.strftime("%d.%m.%Y")}'
            page.update()

    def handle_return_change(e):
        nonlocal return_date
        selected_date = e.control.value
        if selected_date:
            return_date = selected_date.date()
            return_date_text.value = f'{return_date.strftime("%d.%m.%Y")}'
            page.update()

    start_fly = ft.Container(
        date_text, width=145, height=40, alignment=ft.alignment.bottom_center, bgcolor='white',
        on_click=lambda e: page.open(ft.DatePicker(
            confirm_text='Выбрать',
            cancel_text='Отменить',
            first_date=datetime.datetime.today(),
            last_date=datetime.datetime(year=today.year + 1, month=today.month, day=today.day),
            on_change=handle_change
        ))
    )

    return_fly = ft.Container(
        return_date_text, width=145, height=40, alignment=ft.alignment.bottom_center, bgcolor='white',
        on_click=lambda e: page.open(ft.DatePicker(
            confirm_text='Выбрать',
            cancel_text='Отменить',
            first_date=datetime.datetime.today(),
            last_date=datetime.datetime(year=today.year + 1, month=today.month, day=today.day),
            on_change=handle_return_change
        ))
    )

    def update_flight(e):
        flight_id = int(flight_id_input.value) if flight_id_input.value.isdigit() else None
        new_from_city = fromf.value
        new_to_city = tof.value
        new_departure_date = departure_date
        new_return_date = return_date

        if flight_id:
            session = Session()
            flight = session.query(Flight).filter(Flight.id == flight_id).first()

            if flight:
                updated = False

                if new_from_city and new_from_city in cities:
                    flight.from_city = new_from_city
                    updated = True

                if new_to_city and new_to_city in cities:
                    flight.to_city = new_to_city
                    updated = True

                if new_departure_date:
                    flight.departure_date = new_departure_date
                    updated = True

                if new_return_date:
                    flight.return_date = new_return_date
                    updated = True

                if updated:
                    try:
                        if ((tof.value != '' and tof.value not in cities) or
                                fromf.value != '' and fromf.value not in cities):
                            show_snackbar(page, 'Некорректный город', textcolor='red', textsize=23)

                        elif tof.value == fromf.value:
                            show_snackbar(page, 'Города не должны совпадать', textcolor='red', textsize=23)

                        else:
                            session.commit()
                            show_snackbar(page, f"Рейс с ID {flight_id} успешно обновлен.", textsize=20)
                    except Exception as e:
                        session.rollback()
                        show_snackbar(page, f"Ошибка при обновлении рейса: {str(e)}", textsize=20)
                else:
                    show_snackbar(page, "Данные не заполнены", textsize=25)
            else:
                show_snackbar(page, f"Рейс с ID {flight_id} не найден.", textsize=25)

            session.close()
        else:
            show_snackbar(page, 'Введите корректный ID', textsize=25)

    update_button = ft.Container(
        ft.Text('Обновить рейс', style=style(), size=20), width=300, height=50,
        on_click=update_flight,
        border_radius=20, alignment=ft.alignment.center,
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=30, color=colors['block_shadow']),
        bgcolor=colors['bg']
    )

    to = ft.Stack(
        [from_suggestions_list, ft.Column([fromf], alignment=ft.MainAxisAlignment.CENTER)],
        width=300, height=150)

    fromm = ft.Stack(
        [tof, ft.Column([to_suggestions_list], alignment=ft.MainAxisAlignment.CENTER)],
        width=300, height=180)

    date_row = ft.Row(controls=[start_fly, ft.Text('-', style=style()), return_fly],
                      alignment=ft.MainAxisAlignment.CENTER)


    flight_info_section = ft.Column(controls=[
        to,
        fromm
    ], alignment=ft.MainAxisAlignment.CENTER)

    return ft.View(
        route='/admin_mainscreen',
        bgcolor=colors['bg'],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Container(height=150, width=20, bgcolor=colors['bg']),
            flight_id_input,
            flight_info_section,
            date_row,
            ft.Container(height=20, width=20, bgcolor=colors['bg']),
            update_button
        ],
    )
