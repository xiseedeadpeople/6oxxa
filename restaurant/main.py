import flet as ft

from Views.Tabs.UserTabs import closest_flights, my_orders, notifications, main_tab
from Views.main_screen import mainscreen
from Views.login_screen import login_screen


def main(page: ft.Page):
    page.window.width = 390
    page.window.height = 844
    page.window.always_on_top = True
    page.window.maximizable = False
    page.window.resizable = False
    page.padding = 0
    page.spacing = 0

    page.fonts = {
        "TravelingTypewriter": "fonts/TravelingTypewriter.ttf"
    }

    def route_change(route):
        page.views.clear()
        page.views.append(login_screen(page))

        if page.route == "/user_mainscreen":
            page.views.append(mainscreen(page))

        # user tabs
        elif page.route == '/user_mainscreen/main_tab':
            page.views.append(main_tab(page))
        elif page.route == '/user_mainscreen/closest_flights':
            page.views.append(closest_flights(page))
        elif page.route == '/user_mainscreen/my_orders':
            page.views.append(my_orders(page))
        elif page.route == '/user_mainscreen/notifications':
            page.views.append(notifications(page))

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
