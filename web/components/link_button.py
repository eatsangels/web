import reflex as rx
import web.styles.styles as styles
from web.styles.styles import size
from web.styles.colors import Color


def link_button(title: str, body: str, image: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=size.LARGE.value,
                    height=size.LARGE.value,
                    margin=size.MEDIUM.value,
                    alt=title
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    align_items="start",
                    spacing=size.SMALL.value,
                    padding_y=size.SMALL.value,
                    padding_right=size.SMALL.value
                ),
                width="100%"
            )
        ),
        href=url,
        is_external=True,
        width="100%"
    )

    
    