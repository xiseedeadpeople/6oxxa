import flet as ft
import datetime
from prefs.stylesnhelpers import colors, style, error_style, cities, show_snackbar
from models import Session, Flight


def admin_create(page: ft.Page):

    from_suggestions_list = ft.Row()
    to_suggestions_list = ft.Row()

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
        fill_color=colors['bg'])

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
        on_change=tof_changed)

    to = ft.Stack(
        [from_suggestions_list, ft.Column([fromf], alignment=ft.MainAxisAlignment.CENTER)],
        width=300, height=150)

    fromm = ft.Stack(
        [tof, ft.Column([to_suggestions_list], alignment=ft.MainAxisAlignment.CENTER)],
        width=300, height=180)

    today = datetime.datetime.today()
    departure_date = None
    return_date = None

    # date_text = ft.Text(f'{today.strftime("%d.%m.%Y")}', style=style())
    # return_date_text = ft.Text(f'{today.strftime("%d.%m.%Y")}', style=style())
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
        )))

    return_fly = ft.Container(
        return_date_text, width=145, height=40, alignment=ft.alignment.bottom_center, bgcolor='white',
        on_click=lambda e: page.open(ft.DatePicker(
            confirm_text='Выбрать',
            cancel_text='Отменить',
            first_date=datetime.datetime.today(),
            last_date=datetime.datetime(year=today.year + 1, month=today.month, day=today.day),
            on_change=handle_return_change
        )))

    def proverka(e):
        if tof.value not in cities or fromf.value not in cities:
            show_snackbar(page, 'Некорректный город', textcolor='red', textsize=23)

        elif tof.value == fromf.value:
            show_snackbar(page, 'Города не должны совпадать', textcolor='red', textsize=23)

        elif departure_date is None or return_date is None:
            show_snackbar(page, 'Некорректная дата', textcolor='red', textsize=23)

        elif departure_date == return_date:
            show_snackbar(page, 'Даты не должны совпадать', textcolor='red', textsize=23)

        elif (datetime.datetime.strptime(f'{departure_date}', '%Y-%m-%d') >
              datetime.datetime.strptime(f'{return_date}', '%Y-%m-%d')):
            show_snackbar(page, 'Некорректные даты', textcolor='red', textsize=23)

        else:
            print(departure_date, return_date)
            session = Session()
            new_flight = Flight(
                from_city=fromf.value,
                to_city=tof.value,
                departure_date=departure_date,
                return_date=return_date)

            session.add(new_flight)
            session.commit()
            session.close()
            show_snackbar(page, 'Рейс успешно зарегестрирован!', textsize=20)

    searchbtn = ft.Container(
        ft.Text('Создать рейс', style=style(), size=20), width=300, height=50,
        on_click=proverka,
        border_radius=20, alignment=ft.alignment.center,
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=30, color=colors['block_shadow']),
        bgcolor=colors['bg'])

    date_row = ft.Row(controls=[start_fly, ft.Text('-', style=style()), return_fly],
                      alignment=ft.MainAxisAlignment.CENTER)

    return ft.View(
        route='/admin_mainscreen',
        bgcolor=colors['bg'],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            to,
            fromm,
            date_row,
            ft.Container(height=20, width=20, bgcolor=colors['bg']),
            searchbtn
        ],
    )
