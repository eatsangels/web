import reflex as rx
from web.styles.styles import size
from web.styles.colors import Color, TextColor


def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.span(
            title,
            font_weight="bold",
            color=Color.PRIMARY.value
        ),
        f" {body}",
        font_size=size.MEDIUM.value,
        color=TextColor.BODY.value
    )
