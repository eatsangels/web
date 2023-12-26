import reflex as rx
import datetime
import web.constants as const
from web.styles.styles import size
from web.styles.colors import Color, TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="logoedward.png",
            height=size.VERY_BIG.value,
            width=size.VERY_BIG.value,
            alt="Logotipo de EdwardTrinidad. Una \"eme\" entre llaves."
        ),
        rx.link(
            rx.box(
                f"© 2014-{datetime.date.today().year} ",
                rx.span("EdwardTrinidad by Desarrollador.", color=Color.PRIMARY.value),
                " v3."
            ),
            href=const.EdwardTrinidad_URL,
            is_external=True,
            font_size=size.MEDIUM.value
        ),
        rx.text(
            "BUILDING SOFTWARE WITH ♥ FROM CANADA TO THE WORLD.",
            font_size=size.MEDIUM.value,
            margin_top=size.ZERO.value
        ),
        margin_bottom=size.BIG.value,
        padding_bottom=size.BIG.value,
        padding_x=size.BIG.value,
        spacing=size.DEFAULT.value,
        color=TextColor.FOOTER.value
    )
