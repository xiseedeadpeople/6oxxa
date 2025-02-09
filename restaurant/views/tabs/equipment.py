import flet as ft
from prefs.colors import colors, style


class ExpandableItem:
    def __init__(self, name, options):
        self.name = name
        self.options = options
        self.buttons = {}

    def create(self):
        option_column = ft.Column(visible=False)


        for option in self.options:
            button_text = ft.Text('Включить', style=style(size=12))
            button_container = ft.Container(
                content=ft.Row(
                    [button_text],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                bgcolor=colors['bg'],
                shadow=ft.BoxShadow(spread_radius=1, blur_radius=5, color=colors['block_shadow']),
                padding=10,
                border_radius=5,
                width=100,
                height=33,
                on_click=lambda e, opt=option, btn_text=button_text: self.toggle_option(opt, btn_text)
            )

            self.buttons[option] = button_text

            row = ft.Row(
                [
                    ft.Text(option, style=style(size=12)),
                    button_container
                ],
                alignment=ft.MainAxisAlignment.END,
                height=50
            )
            option_column.controls.append(row)

        item_row = ft.Container(
            content=ft.Row(
                [
                    ft.Text(self.name, style=style(size=15)),
                    ft.IconButton(
                        icon=ft.icons.EXPAND_MORE,
                        icon_color=colors['primary'],
                        on_click=lambda e: self.toggle_expansion(e, option_column),
                        data=option_column,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                height=60,

            ),
            shadow=ft.BoxShadow(spread_radius=1, blur_radius=5, color=colors['block_shadow']),
            padding=10,
            bgcolor=colors['bg'],
            width=350,
            height=150,
            border_radius=20,
        )

        item_row.on_click = lambda e: self.toggle_expansion(e, option_column)
        return ft.Column([item_row, option_column])

    @staticmethod
    def toggle_expansion(e, option_column):
        option_column.visible = not option_column.visible
        e.page.update()


    @staticmethod
    def toggle_option(option, button_text):
        if button_text.value == 'Включить':
            button_text.value = 'Выключить'
        else:
            button_text.value = 'Включить'
        button_text.update()


def equipment(page: ft.Page):
    page.horizontal_alignment = 'center'

    list_view = ft.ListView(
        spacing=10,
        controls=[ExpandableItem('Кухня', ['Умный холодильник', 'Умная плита', 'Системы управления запасами']).create(),
                  ExpandableItem('Безопасность и контроль', ['Камеры', 'Температура холодильника']).create()]
    )

    return ft.View(
        route='/user_mainscreen',
        bgcolor=colors['bg'],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[ft.Container(height=150, bgcolor=colors['bg']), list_view], spacing=0)
