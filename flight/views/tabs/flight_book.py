import flet as ft
import datetime
from prefs.colors import colors, style, error_style

def flight_book(page: ft.Page):
    cities = [
        "Москва", "Санкт-Петербург", "Екатеринбург", "Новосибирск", "Краснодар", "Сочи",
        "Благовещенск", "Владивосток", "Красноярск", "Улан-Удэ", "Уфа", "Омск"
    ]

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

    def fon_focus(e):
        fromf.error_text = ''
        page.update()

    def ton_focus(e):
        tof.error_text = ''
        page.update()

    fromf = ft.TextField(
        cursor_color='black',
        focused_color='black',
        label='Откуда',
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
        label='Куда',
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

    formatted_date = None
    formatted_return_date = None

    def handle_change(e):
        nonlocal formatted_date
        selected_date = e.control.value
        formatted_date = selected_date.strftime('%d/%m/%Y')
        date_text.value = f'{formatted_date}'
        page.update()

    def handle_return_change(e):
        nonlocal formatted_return_date
        selected_date = e.control.value
        formatted_return_date = selected_date.strftime('%d/%m/%Y')
        return_date_text.value = f'{formatted_return_date}'
        page.update()

    today = datetime.datetime.today()
    date_text = ft.Text(f'{today.strftime("%d/%m/%Y")}', style=style())
    return_date_text = ft.Text(f'{today.strftime("%d/%m/%Y")}', style=style())

    start_fly = ft.Container(
        date_text, width=145, height=40 ,alignment=ft.alignment.bottom_center, bgcolor='white',
        on_click=lambda e: page.open(ft.DatePicker(
            confirm_text='Выбрать',
            cancel_text='Отменить',
            first_date=datetime.datetime(year=today.year, month=today.month, day=today.day),
            last_date=datetime.datetime(year=today.year + 1, month=today.month, day=today.day),
            on_change=handle_change)))

    return_fly = ft.Container(
        return_date_text, width=145, height=40, alignment=ft.alignment.bottom_center, bgcolor='white',
        on_click=lambda e: page.open(ft.DatePicker(
            confirm_text='Выбрать',
            cancel_text='Отменить',
            first_date=datetime.datetime(year=today.year, month=today.month, day=today.day),
            last_date=datetime.datetime(year=today.year + 1, month=today.month, day=today.day),
            on_change=handle_return_change)))

    def proverka(e):
        # if tof.value == fromf.value:
        #     tof.error_text = 'Города не должны совпадать!'
        #     fromf.error_text = 'Города не должны совпадать!'
        #
        # else:
        print(f'{fromf.value} - {tof.value} : {formatted_date} - {formatted_return_date}')

    searchbtn = ft.Container(
        ft.Text('Найти билеты', style=style(), size=20), width=300, height=50,
        on_click=proverka,
        border_radius=20, alignment=ft.alignment.center,
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=30, color=colors['block_shadow']),
        bgcolor=colors['bg'])

    date_row = ft.Row(controls=[start_fly, ft.Text('-', style=style()), return_fly],
        alignment=ft.MainAxisAlignment.CENTER)

    return ft.View(
        route='/user_mainscreen',
        bgcolor=colors['bg'],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            to,
            fromm,
            date_row,
            ft.Container(height=20, width=20, bgcolor='white'),
            searchbtn
        ],

    )
