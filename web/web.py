import reflex as rx
from web.components.navbar import navbar
from web.components.footer import footer
from web.views.header.header import header
from web.views.links.links import links
from web.views.sponsors.sponsors import sponsors

import web.styles.styles as styles
from web.styles.styles import size as size


# class   State(rx.State):
#     pass



def index() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=size.BIG.value,
                padding=size.BIG.value
            )
        ),
        footer()
    )
           
      

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    head_components=[
        rx.script(src="https://www.googletagmanager.com/gtag/js?id=G-3YGHT3XJFS"),
        rx.script(
            """
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-3YGHT3XJFS');
"""
        ),
    ],
)

app.add_page(
    index,
     title="Edward Trinidad | soy desarrollo de software",
    description="Hola, mi nombre es Edward Trinidad. Soy ingeniero de software, desarrollador freelance full-stack.",
    image="avatar.png"

)
app.compile()  