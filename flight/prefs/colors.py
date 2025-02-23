import flet as ft
colors = {
    # 'primary': '#5117FF',
    # 'secondary': '#1e3028',
    # 'bg': '#111111',
    # 'font_shadow': '#5117FF',
    # 'gradient': ['#abff9e', '#000000'],
    # 'second_shadow': '#abff9e',
    # 'error': '#ff0000',
    # 'error_shadow': '#7B0909',
    # 'block_shadow': '#000000',
    # 'inv_primarytext': '#000000',
    # 'inv_fontshadow': '#AF94FF',

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

def style(color=None, size=25, font_family='regular', shadowclr=None, spreadshadow=10):
    if color is None:
        color = colors['primary']
    if shadowclr is None:
        shadowclr = colors['font_shadow']
    return ft.TextStyle(color=color, size=size, font_family=font_family, decoration=ft.TextDecoration.NONE,
                        shadow=ft.BoxShadow(color=shadowclr, spread_radius=spreadshadow,
                                            offset=(0, 0), blur_radius=4,
                                            blur_style=ft.ShadowBlurStyle.OUTER))


def error_style(color=None, size=25, font_family='regular', shadowclr=None, spreadshadow=10):
    if color is None:
        color = colors['error']
    if shadowclr is None:
        shadowclr = colors['error_shadow']
    return ft.TextStyle(color=color, size=size, font_family=font_family,
                        shadow=ft.BoxShadow(color=shadowclr, spread_radius=spreadshadow,
                                            offset=(0, 0), blur_radius=4,
                                            blur_style=ft.ShadowBlurStyle.OUTER))
