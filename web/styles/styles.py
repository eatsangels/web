import reflex as rx
from enum import Enum
from .colors import Color, TextColor
from .fonts import Font, FontWeight

# Constants
MAX_WIDTH = "560px"

# Sizes

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
]

# sizes
class size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"

#Styles

BASE_STYLE = {
     "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUND.value,
    rx.Heading: {
        "color": TextColor.HEADER.value,
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value
    },
    rx.Button:{
         "width": "100%",
        "height": "100%",
        "padding": size.SMALL.value,
        "border_radius": size.DEFAULT.value,
        "color": TextColor.HEADER.value,
        "background_color": Color.CONTENT.value,
        "white_space": "normal",
        "text_align": "start",
        "_hover": {
        "background_color": Color.SECONDARY.value
        }
        },
    rx.Link: {
        "text_decoration" : "none",
        "_hover": {}
    },
}

title_style = dict(
    width="100%",
    padding_top=size.DEFAULT.value,
    font_size=size.LARGE.value
)

button_title_style = dict(
    font_size=size.DEFAULT.value,
)

button_body_style = dict(
    font_size=size.MEDIUM.value,
)

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=size.LARGE.value
)
