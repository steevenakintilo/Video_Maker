
import json
import os
from pathlib import Path
from base64 import b64decode


from bing_image_downloader import downloader
import openai

import os
import fnmatch

from os import system
from PIL import Image

from decouple import config

def print_full_path_file():
    num = "0123456789"
    directory = 'images/my_image'

    files = list(os.listdir(directory))
    n = 0
    full = []
    for file in files:
        full_path = os.path.join(directory, file)
        full.append(str(full_path))
    return (full)


def make_image(pic_req):
    PROMPT = pic_req
    DATA_DIR = Path.cwd() / "responses"

    DATA_DIR.mkdir(exist_ok=True)

    openai.api_key = config('OPEN_IA_KEY')

    try:
        response = openai.Image.create(
            prompt=PROMPT,
            n=1,
            size="512x512",
            response_format="b64_json",
        )

        file_name = DATA_DIR / "my_image.json"

        with open(file_name, mode="w", encoding="utf-8") as file:
            json.dump(response, file)


        DATA_DIR = Path.cwd() / "responses"
        JSON_FILE = DATA_DIR / "my_image.json"
        IMAGE_DIR = Path.cwd() / "images" / JSON_FILE.stem

        IMAGE_DIR.mkdir(parents=True, exist_ok=True)

        with open(JSON_FILE, mode="r", encoding="utf-8") as file:
            response = json.load(file)

        for index, image_dict in enumerate(response["data"]):
            image_data = b64decode(image_dict["b64_json"])
            image_file = IMAGE_DIR / f"my_image_{str(pic_req).strip()}.png"
            with open(image_file, mode="wb") as png:
                png.write(image_data)
    except:
        pass