import flet as ft


class ExpandableItem:
    def __init__(self, name, options):
        self.name = name
        self.options = options

    def create(self):
        option_column = ft.Column(visible=False)

        # options customization
        for option in self.options:
            row = ft.Row(
                [
                    ft.Text(option, color='black'),
                    ft.ElevatedButton('Включить', color='black', bgcolor='#2bff88', on_click=lambda e, opt=option: self.enable_option(opt)),
                ],
                alignment=ft.MainAxisAlignment.END,
                height=50
            )
            option_column.controls.append(row)

        item_row = ft.Container(
            content=ft.Row(
                [
                    ft.Text(self.name, color='#36618e', size=20),
                    ft.IconButton(
                        icon=ft.icons.EXPAND_MORE,
                        on_click=lambda e: self.toggle_expansion(e, option_column),
                        data=option_column,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                height=60,
            ),
            padding=10,
            bgcolor='#f2f3fa',
            width=350,
            height=150,
            border_radius=20,
        )

        item_row.on_click = lambda e: self.toggle_expansion(e, option_column)
        return ft.Column([item_row, option_column])

    def toggle_expansion(self, e, option_column):
        option_column.visible = not option_column.visible
        e.page.update()

    def enable_option(self, option):
        print(f"Опция '{option}' включена!")


def equipment(page: ft.Page):
    page.window.width = 390
    page.window.height = 844
    page.window.always_on_top = True
    page.window.maximizable = False
    page.window.resizable = False
    page.bgcolor = 'black'
    page.padding = 20
    page.spacing = 20

    page.horizontal_alignment = 'center'

    list_view = ft.ListView(
        spacing=10,
        controls=[
            item.create() for item in [
                ExpandableItem('Кухня', ['Умный холодильник', 'Умная плита', 'Системы управления запасами']),
                ExpandableItem('Безопасность и контроль', ['Камеры', 'Температура холодильника'])
            ]
        ]
    )

    return ft.View(
        route='/user_mainscreen',
        bgcolor='#FFFFFF',
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

        controls=[ft.Container(height=150, bgcolor='#FFFFFF'), list_view], spacing=0
    )
