import flet as ft
import codecs

fileObj = codecs.open( "prefs/txt-cities-russia.txt", "r", "utf_8_sig" )
text = fileObj.readlines()
fileObj.close()
cities = list(map(str.strip, text))


colors = {
    'primary': '#000000',
    'secondary': '#1e3028',
    'bg': '#FFFFFF',
    'font_shadow': '#929292',
    'gradient': ['#abff9e', '#000000'],
    'second_shadow': '#abff9e',
    'error': '#ff0000',
    'error_shadow': '#7B0909',
    'block_shadow': '#929292',
    'inv_primarytext': '#000000',
    'inv_fontshadow': '#AF94FF',
}


def style(color=None, size=25, font_family='primary', shadowclr=None, spreadshadow=10):
    if color is None:
        color = colors['primary']
    if shadowclr is None:
        shadowclr = colors['font_shadow']
    return ft.TextStyle(color=color, size=size, font_family=font_family, decoration=ft.TextDecoration.NONE,
                        shadow=ft.BoxShadow(color=shadowclr, spread_radius=spreadshadow,
                                            offset=(0, 0), blur_radius=4,
                                            blur_style=ft.ShadowBlurStyle.OUTER))


def error_style(color=None, size=25, font_family='primary', shadowclr=None, spreadshadow=10):
    if color is None:
        color = colors['error']
    if shadowclr is None:
        shadowclr = colors['error_shadow']
    return ft.TextStyle(color=color, size=size, font_family=font_family,
                        shadow=ft.BoxShadow(color=shadowclr, spread_radius=spreadshadow,
                                            offset=(0, 0), blur_radius=4,
                                            blur_style=ft.ShadowBlurStyle.OUTER))

def show_snackbar(page, message, textsize=15, textcolor='white', ff='regular', bgcolor='black'):
    snackbar = ft.SnackBar(
        ft.Container(ft.Text(message, style=style(size=textsize, color=textcolor, shadowclr=bgcolor,
                                                  font_family=ff)), alignment=ft.alignment.center),
        open=True, bgcolor=bgcolor, duration=1000
    )
    page.overlay.append(snackbar)
    page.update()

def tfield(label, ):
    return ft.TextField(
        cursor_color='black',
        focused_color='black',
        label=f'{label}',
        width=300,
        border_radius=10,
        label_style=style(),
        text_style=style(),
        prefix_style=style(color='black'),
        error_style=error_style(size=10, shadowclr=colors['bg']),
        adaptive=True,
        border=ft.InputBorder.NONE,
        fill_color=colors['bg'],
    )


