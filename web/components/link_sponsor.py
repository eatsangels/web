import reflex as rx
from web.styles.styles import size


def link_sponsor(imagen: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=imagen,
            height=size.VERY_BIG.value,
            aspect_ratio="5 / 2",
            alt=alt
        ),
        href=url,
        is_external=True
    )
