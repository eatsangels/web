import reflex as rx
import web.styles.styles as styles
from web.styles.styles import size
from web.styles.colors import Color

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.span("Edward", color=Color.PRIMARY.value),
            rx.span("Trinidad", color=Color.SECONDARY.value),
            style=styles.navbar_title_style,
            image="avatar.png"
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=size.BIG.value,
        padding_y=size.DEFAULT.value,
        z_index="999",
        top="0"
    )
