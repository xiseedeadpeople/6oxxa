import flet as ft
from datetime import datetime

today = datetime.today().date().strftime('%d.%m.%Y')


def reservation(page):
    page.window.width = 390
    page.window.height = 844
    page.window.always_on_top = True
    page.window.maximizable = False
    page.window.resizable = False
    page.padding = 0
    page.spacing = 0

    def handle_dlg_action_clicked(e):
        page.close(dlg)
        dlg.data.confirm_dismiss(e.control.data)

    dlg = ft.CupertinoAlertDialog(
        modal=True,
        title=ft.Text("Пожалуйста, подтвердите"),
        content=ft.Text("Вы действительно хотите отменить бронь?"),

        actions=[
            ft.CupertinoButton("Да", data=True, on_click=handle_dlg_action_clicked, color='red'),
            ft.CupertinoButton("Нет", data=False, on_click=handle_dlg_action_clicked, color='#36618e'),
        ],
    )

    def handle_confirm_dismiss(e: ft.DismissibleDismissEvent):
        if e.direction == ft.DismissDirection.END_TO_START:  # right-to-left slide
            # save current dismissible to dialog's data, for confirmation in handle_dlg_action_clicked
            dlg.data = e.control
            page.open(dlg)
        else:  # left-to-right slide
            e.control.confirm_dismiss(True)

    def handle_dismiss(e):
        e.control.parent.controls.remove(e.control)
        page.update()

    def handle_update(e: ft.DismissibleUpdateEvent):
        print(
            f"dir: {e.direction}, progress: {e.progress}, reached: {e.reached}, previous_reached: {e.previous_reached}"
        )

    lww = ft.ListView(
            expand=True,
            controls=[
                ft.Dismissible(
                    content=ft.ListTile(
                        title=ft.Container(
                            content=ft.Text(f"Бронь {today} - {i}", color='#36618e', size=25),
                            alignment=ft.alignment.center,
                            bgcolor='#ffffff',
                            height=75,
                            padding=0,
                        )
                    ),
                    dismiss_direction=ft.DismissDirection.HORIZONTAL,
                    background=ft.Container(bgcolor='#2bff88'),
                    secondary_background=ft.Container(bgcolor=ft.colors.RED),
                    on_dismiss=handle_dismiss,
                    on_update=handle_update,
                    on_confirm_dismiss=handle_confirm_dismiss,
                    dismiss_thresholds={
                        ft.DismissDirection.END_TO_START: 0.2,
                        ft.DismissDirection.START_TO_END: 0.2,
                    }
                )
                for i in range(1, 25)
            ],
            spacing=10,
            width=360,
            first_item_prototype=True,
            height=635
        )

    return ft.View(
        route='/user_mainscreen',
        bgcolor='#ffffff',
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

        controls=[ft.Container(height=150), lww, ft.Container(height=10)]
    )



