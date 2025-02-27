import flet as ft
import datetime
from prefs.stylesnhelpers import colors, style, error_style, cities, show_snackbar
from models import Session, Flight, PurchaseHistory




def main_screen(page: ft.Page):
    def youchangechoice(e):
        youindex = e.control.selected_index

        if youindex == 0:
            page.go('/user_mainscreen/flight_book')

        if youindex == 1:
            page.go('/user_mainscreen/closest_flights')

        page.update()

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
    date_text = ft.Text(f'Вылет', style=style())
    return_date_text = ft.Text(f'Прилёт', style=style())

    start_fly = ft.Container(
        date_text, width=145, height=40, alignment=ft.alignment.bottom_center, bgcolor='white',
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

    history_list_view = ft.ListView(expand=True, spacing=10, width=360, first_item_prototype=True, height=635)


    def proverka(e):
        if formatted_date is None or formatted_return_date is None:
            show_snackbar(page, 'Некорректная дата', textcolor='red', textsize=23)

        else:
            departure_date = datetime.datetime.strptime(str(formatted_date), '%d/%m/%Y').date()
            return_date = datetime.datetime.strptime(str(formatted_return_date), '%d/%m/%Y').date()

            if tof.value not in cities or fromf.value not in cities:
                show_snackbar(page, 'Некорректный город', textcolor='red', textsize=23)

            elif tof.value == fromf.value:
                show_snackbar(page, 'Города не должны совпадать', textcolor='red', textsize=23)


            elif departure_date == return_date:
                show_snackbar(page, 'Даты не должны совпадать', textcolor='red', textsize=23)

            elif (datetime.datetime.strptime(f'{departure_date}', '%Y-%m-%d') >
                  datetime.datetime.strptime(f'{return_date}', '%Y-%m-%d')):
                show_snackbar(page, 'Некорректные даты', textcolor='red', textsize=23)

            else:
                session = Session()
                flights = session.query(Flight).filter(
                    Flight.from_city == fromf.value,
                    Flight.to_city == tof.value,
                    Flight.departure_date == departure_date,
                    Flight.return_date == return_date
                ).all()

                session.close()

                if flights:
                    show_snackbar(page, 'Билеты найдены (Куплены)', textsize=20)
                    session = Session()
                    purchase = PurchaseHistory(
                        from_city=fromf.value,
                        to_city=tof.value,
                        departure_date=departure_date,
                        return_date=return_date
                    )

                    session.add(purchase)
                    session.commit()
                    session.close()

                else:
                    show_snackbar(page, 'Билетов не найдено!', textsize=23)


    searchbtn = ft.Container(
        ft.Text('Найти билеты', style=style(), size=20), width=300, height=50,
        on_click=proverka,
        border_radius=20, alignment=ft.alignment.center,
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=30, color=colors['block_shadow']),
        bgcolor=colors['bg'])

    date_row = ft.Row(controls=[start_fly, ft.Text('-', style=style()), return_fly],
                      alignment=ft.MainAxisAlignment.CENTER)


    mytab = ft.Tabs(
        tab_alignment=ft.TabAlignment.FILL,
        selected_index=0,
        animation_duration=300,
        unselected_label_color=colors['secondary'],
        label_color=colors['primary'],
        indicator_color=colors['primary'],
        indicator_border_radius=30,
        divider_height=0,
        scrollable=True,
        on_change=youchangechoice,

        tabs=[ft.Tab(text='Главная страница')]
    )

    def open_repo(e):
        page.launch_url('https://github.com/xiseedeadpeople/6oxxa/tree/main/flight')

    github = ft.Container(
        content=ft.Image(src="prefs/icons/github.ico"), on_click=open_repo, padding=10)

    mybar = ft.Container(
        bgcolor=colors['bg'],
        border_radius=ft.border_radius.vertical(bottom=30),
        shadow=ft.BoxShadow(spread_radius=1, blur_radius=100, color=colors['block_shadow']),
        width=page.window.width,
        height=150,
        padding=10,

        content=ft.Column([
            ft.Row([github,
                    ft.Text('cvvmoney✦₊',
                            style=style(color=colors['primary'],
                                        shadowclr=colors['font_shadow'], size=20))]),
            mytab],

            alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    )

    page.overlay.append(mybar)
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
