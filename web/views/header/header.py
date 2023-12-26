import reflex as rx
import datetime
import web.constants as const
from web.styles.styles import size
from web.styles.colors import Color, TextColor
from web.components.link_icon import link_icon
from web.components.info_text import info_text


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Edward Trinidad",
                size="xl",
                src="avatar.png",
                color=TextColor.BODY.value,
                bg=Color.CONTENT.value,
                padding="2px",
                border="4px",
                border_color=Color.PRIMARY.value
            ),
            rx.vstack(
                rx.heading(
                    "Edward Trinidad",
                    size="lg"
                ),
                rx.text(
                    "@Edward_Trinidad!",
                    margin_top=size.ZERO.value,
                    color=Color.PRIMARY.value
                ),
                rx.hstack(
                    link_icon(
                        "icons/github.svg",
                        const.GITHUB_URL,
                        "GitHub"
                    ),
                    link_icon(
                        "icons/x.svg",
                        const.TWITTER_X_URL,
                        "Twitter/X"
                    ),
                    link_icon(
                        "icons/instagram.svg",
                        const.INSTAGRAM_URL,
                        "Instagram"
                    ),
                    link_icon(
                        "icons/tiktok.svg",
                        const.TIKTOK_URL,
                        "TikTok"
                    ),
                    link_icon(
                        "icons/spotify.svg",
                        const.SPOTIFY_URL,
                        "Spotify"
                    ),
                    link_icon(
                        "icons/linkedin.svg",
                        const.LINKEDIN_URL,
                        "LinkedIn"
                    ),
                    spacing=size.LARGE.value
                ),
                align_items="start"
            ),
            spacing=size.DEFAULT.value
        ),
        rx.flex(
            info_text(
                f"{experience()}+",
                "años de experiencia"
            ),
            rx.spacer(),
            info_text(
                "100+", "aplicaciones creadas"
            ),
            rx.spacer(),
            info_text(
                "1M+", "seguidores"
            ),
            width="100%"
        ),
        rx.text(
            f"""
            Como ingeniero de software, mi rol es fundamental en el desarrollo de aplicaciones y programas. Mi capacidad para diseñar, escribir y probar código es crucial para el éxito de los proyectos en los que participo. Trabajo en estrecha colaboración con otros profesionales, aportando mi experiencia técnica y habilidades de resolución de problemas para crear soluciones innovadoras. Además, mi compromiso con la mejora continua y el aprendizaje de nuevas tecnologías me distingue como un profesional dedicado y apasionado por mi trabajo.! ¡Bienvenid@!
            """,
            font_size=size.DEFAULT.value,
            color=TextColor.BODY.value
        ),
        spacing=size.BIG.value,
        align_items="start"
    )


def experience() -> int:
    return datetime.date.today().year - 2010
