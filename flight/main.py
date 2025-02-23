import flet as ft

from views.loginscreen import login_screen
from views.mainscreen import main_screen

from views.tabs.orders_history import ordrs_history
from views.tabs.flight_book import flight_book
from views.tabs.closest_flights import closest_flights

#   itertools , combinations_with_replacement
#   concurrent.futures , ProcessPoolExecutor
#   multiprocessing


def main(page: ft.Page):
    page.window.width = 390
    page.window.height = 844
    page.window.always_on_top = True
    page.window.maximizable = False
    page.window.resizable = False
    page.padding = 0
    page.spacing = 0

    def route_change(route):
        page.views.clear()

        if page.route == '/':
            page.views.append(login_screen(page))

        elif page.route == "/user_mainscreen":
            page.views.append(main_screen(page))

        elif page.route == '/user_mainscreen/closest_flights':
            page.views.append(closest_flights(page))

        elif page.route == '/user_mainscreen/ordrs_history':
            page.views.append(ordrs_history(page))

        elif page.route == '/user_mainscreen/flight_book':
            page.views.append(flight_book(page))

        page.update()


    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)
