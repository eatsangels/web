import reflex as rx
import web.constants as const
from web.styles.styles import size
from web.components.title import title
from web.components.link_sponsor import link_sponsor


def sponsors() -> rx.Component:
    return rx.vstack(
        title("Colaboran"),
        rx.responsive_grid(
            link_sponsor(
                "elgato.png",
                const.NOTENGO_URL,
                "Logotipo de Elgato"
            ),
            link_sponsor(
                "mvp.png",
                const.PRONTO_URL,
                "Logotipo de Microsoft MVP"
            ),
            spacing=size.BIG.value,
            columns=[1, 2]
        ),
        width="100%",
        align_items="start",
        spacing=size.MEDIUM.value
    )
