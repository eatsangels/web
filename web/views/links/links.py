import reflex as rx
import web.constants as const
from web.components.link_button import link_button
from web.components.title import title
from web.styles.styles import size
from web.components.link_button import link_button


def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(
            "Twitch",
            "Transmisiones sobre programación de lunes a viernes",
            "icons/twitch.svg",
            const.TWITCH_URL
        ),
        link_button(
            "YouTube",
            "Tutoriales sobre desarrollo de software semanales",
            "icons/youtube.svg",
            const.YOUTUBE_URL
        ),
        link_button(
            "Discord",
            "El chat y los grupos de estudio de la comunidad",
            "icons/discord.svg",
            const.DISCORD_URL
        ),
        link_button(
            "Retos de programación",
            "Ejercicios semanales para practicar lógica de programación",
            "icons/code.svg",
            const.CODE_CHALLENGES_URL
        ),
        link_button(
            "YouTube ⓘ canal secundario",
            "Emisiones en directo destacadas",
            "icons/youtube.svg",
            const.YOUTUBE_SECONDARY_URL
        ),

        title("Recursos y más"),
        link_button(
            "Git y GitHub desde cero",
            "Aquí puedes comprar mi libro en formato físico y eBook",
            "icons/git.svg",
            const.BOOK_URL
        ),
        link_button(
            "Libros recomendados",
            "Mi listado de libros sobre programación, ciencia y tecnología",
            "icons/book.svg",
            const.BOOKS_URL
        ),
        link_button(
            "Mi setup",
            "Listado con todos los elementos que uso en mi trabajo",
            "icons/setup.svg",
            const.SETUP_URL
        ),
        link_button(
            "EdwardTrinidad",
            "Mi sitio web",
            "icons/logo.png",
            const.EdwardTrinidad_URL
        ),
        link_button(
            "Invítame a un café",
            "¿Quieres ayudarme a que siga creando contenido?",
            "icons/coffee.svg",
            const.COFFEE_URL
        ),

        title("Contacto"),
        link_button(
            "MyPublicInbox",
            "Respuesta rápida y con preferencia",
            "icons/checkemail.svg",
            const.MYPUBLICINBOX_URL
        ),
        link_button(
            "Email",
            const.EMAIL,
            "icons/email.svg",
            f"mailto:{const.EMAIL}"
        ),
        width="100%",
        spacing=size.DEFAULT.value,
    )
