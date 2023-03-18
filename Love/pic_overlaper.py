import os
import random
from typing import List, Dict, Any
from io import BytesIO
from PIL import Image, ImageFont, ImageDraw

PATH_TO_CORNER_ELEMENTS = "./images/corner_elements"
PATH_TO_BACKGROUNDS = "./images/backgrounds"
PATH_TO_FONTS = "./fonts"
PATH_TO_VIGNETTES = "./images/vignettes"

VALID_CORNER_PICTURES = []
VALID_BACKGROUNDS = []
VALID_FONTS = []
VALID_VIGNETTES = []

for directory, formats, valid_list in [(PATH_TO_CORNER_ELEMENTS, ['png'], VALID_CORNER_PICTURES),
                                       (PATH_TO_BACKGROUNDS, ['jpeg', 'jpg'], VALID_BACKGROUNDS),
                                       (PATH_TO_FONTS, ['ttf', 'otf'], VALID_FONTS),
                                       (PATH_TO_VIGNETTES, ['png'], VALID_VIGNETTES)]:
    for file_name in os.listdir(directory):
        if file_name.endswith(tuple(formats)):
            valid_list.append(os.path.join(directory, file_name))


def get_elements_for_picture() -> Dict[str, Any]:
    font = random.choice(VALID_FONTS)
    corner_pictures = random.sample(VALID_CORNER_PICTURES, k=4)
    background = random.choice(VALID_BACKGROUNDS)
    vignette = random.choice(VALID_VIGNETTES)
    return {"font": font, "corner_pictures": corner_pictures, "background": background, "vignette": vignette}


def paste_corner_elements(card_image: Image.Image, corner_elements: List[str]) -> Image.Image:
    coordinates = [(20, 20), (430, 20), (20, 280), (430, 280)]
    for element, coord in zip(corner_elements, coordinates):
        with Image.open(element).convert("RGBA") as element_to_paste:
            card_image.paste(element_to_paste, coord, element_to_paste)
    return card_image


def draw_text_on_image(card_image: Image.Image, love_phrase: str, font_path: str, color: str) -> None:
    with ImageFont.truetype(font=font_path, size=35) as font:
        draw = ImageDraw.Draw(card_image)
        w, h = draw.textsize(love_phrase, font=font)
        x, y = card_image.size
        draw.text(((x - w) / 2, (y - h) / 2), love_phrase.upper(), font=font, fill=color, align="center")


def draw_vignette(card_image: Image.Image, vignette_path: str) -> Image.Image:
    with Image.open(vignette_path).convert("RGBA") as element_to_paste:
        card_image.paste(element_to_paste, (100, 30), element_to_paste)
    return card_image


def love_func(love_phrase: str):
    picture_ingredients: dict = get_elements_for_picture()
    bg = Image.open(picture_ingredients["background"]).convert("RGBA")  # конверт в red, green, blue, alpha каналы
    corner_elements = picture_ingredients["corner_pictures"]
    vignette = picture_ingredients["vignette"]
    font = picture_ingredients["font"]
    output_content = BytesIO()
    output_content.name = 'output_content.jpeg'

    card = Image.new(mode="RGB", size=bg.size)
    card.paste(bg, (0, 0, *bg.size), bg)
    card = draw_vignette(card, vignette)
    card = paste_corner_elements(card, corner_elements)

    draw_text_on_image(card_image=card, love_phrase=love_phrase, fontpath=font, color="yellow")

    card.save(output_content, 'JPEG')
    output_content.seek(0)
    return output_content
