import flet as ft
from views.loginscreen import login_screen
from views.mainscreen import main_screen

from views.tabs.reservation import reservation
from views.tabs.ordershistory import orders_history
from views.tabs.menu import menu
from views.tabs.equipment import equipment
from views.tabs.staff import staff


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
        page.views.append(login_screen(page))


        if page.route == "/user_mainscreen":
            page.views.append(main_screen(page))

        elif page.route == '/user_mainscreen/reservation':
            page.views.append(reservation(page))

        elif page.route == '/user_mainscreen/orders_history':
            page.views.append(orders_history(page))

        elif page.route == '/user_mainscreen/menu':
            page.views.append(menu(page))

        elif page.route == '/user_mainscreen/equipment':
            page.views.append(equipment(page))

        elif page.route == '/user_mainscreen/staff':
            page.views.append(staff(page))

        # manager tabs

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)


ft.app(target=main)
