import flet as ft
colors = {
    'primary': '#abff9e',
    'secondary': '#1e3028',
    'bg': '#111111',
    'font_shadow': '#4caf50',
    'gradient': ['#000000', '#000000'],
    'gradient2': ['#abff9e', '#000000'],
    'second_shadow': '#abff9e',
    'error': '#ff0000',
    'error_shadow': '#7B0909',
    'block_shadow': '#000000',

    # inversion
    'inv_primarytext': '#000000',
    'inv_fontshadow': '#abff9e',

}

def style(color=None, size=20, font_family='basic', shadowclr=None, spreadshadow=10):
    if color is None:
        color = colors['primary']

    if shadowclr is None:
        shadowclr = colors['font_shadow']

    return ft.TextStyle(color=color, size=size, font_family=font_family, decoration=ft.TextDecoration.NONE,
                        shadow=ft.BoxShadow(color=shadowclr, spread_radius=spreadshadow,
                                            offset=(0, 0), blur_radius=4,
                                            blur_style=ft.ShadowBlurStyle.OUTER))


def error_style(color=None, size=20, font_family='basic', shadowclr=None, spreadshadow=10):
    if color is None:
        color = colors['error']

    if shadowclr is None:
        shadowclr = colors['error_shadow']

    return ft.TextStyle(color=color, size=size, font_family=font_family,
                        shadow=ft.BoxShadow(color=shadowclr, spread_radius=spreadshadow,
                                            offset=(0, 0), blur_radius=4,
                                            blur_style=ft.ShadowBlurStyle.OUTER))
