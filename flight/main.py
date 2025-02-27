import flet as ft

from views.loginscreen import login_screen
from views.mainscreen import main_screen
from views.adminscreen import admin_screen

from views.admin_tabs.admin_create import admin_create
from views.admin_tabs.admin_delete import admin_delete
from views.admin_tabs.admin_update import admin_update

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

        elif page.route == '/admin_mainscreen':
            page.views.append(admin_screen(page))

        elif page.route == '/admin_mainscreen/admin_create':
            page.views.append(admin_create(page))

        elif page.route == '/admin_mainscreen/admin_delete':
            page.views.append(admin_delete(page))

        elif page.route == '/admin_mainscreen/admin_update':
            page.views.append(admin_update(page))

        page.update()


    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)
