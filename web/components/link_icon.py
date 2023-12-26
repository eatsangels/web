import reflex as rx
from web.styles.styles import size


def link_icon(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=size.LARGE.value,
            height=size.LARGE.value,
            alt=alt
        ),
        href=url,
        is_external=True
    )
