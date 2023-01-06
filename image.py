
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

def return_only_num(lst):
    num = "0123456789"
    s = ""
    n = []
    for i in range(len(lst)):
        l = lst[i]
        for j in range(len(l)):
            if l[j] in num:
                s = s + l[j]
        n.append(s)
        s = ""
    n.sort(reverse=True)
    if len(n) != 0:
        return (n[0])
    return ("None")

def print_path_file():
    num = "0123456789"
    directory = 'images/my_image'

    files = list(os.listdir(directory))
    n = 0
    full = []
    for file in files:
        full_path = os.path.join(directory, file)
        full.append(full_path)
    
    if return_only_num(full) == "None":
        return ("1")
    r = return_only_num(full)
    return(int(r)+1)


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


def make_image_(pic_req):
    if not os.path.exists('pic'):
        os.makedirs('pic')

    downloader.download(query=pic_req, limit=1,  adult_filter_off=True, force_replace=False, timeout=60, verbose=True, output_dir='pic')
 


def resize_pic(p):
    l = p.split("/")
    path = l[0]+"/"+l[1]
    path = path.strip()
    with Image.open(p) as im:
        # Resize the image
        im_resized = im.resize((512, 512))
        # Save the resized image to a new file
        im_resized.save(path+"/"+"resize_pic.jpg")
    #system("rm " + str(p))
    return(path+"/"+"resize_pic.jpg")

def resize_and_save(path):
    # Open the image
    with Image.open(path) as im:
        # Resize the image
        im_resized = im.resize((512, 512))
        # Save the resized image to a new file
        im_resized.save(path+"_resized.jpg")
    # Remove the old image
    os.remove(path)
    return(path+"_resized.jpg")


def print_path_pic():
    root_folder = 'pic'
    pattern = '*.jpg'
    matching_files = []
    m = []
    for root, dirs, files in os.walk(root_folder):
        if root != "" and "jpg" in str(files):
            print(files)
            matching_files.append(root+"/"+str(files).replace("[","").replace("]","").replace("'",""))
    for i in range(len(matching_files)):
        m.append(resize_and_save(matching_files[i]))
    #print(m)
    filtered_list = [x for x in m if x is not None]
    return (filtered_list)
    #for filename in fnmatch.filter(files, pattern):
    #    file_path = os.path.join(root, filename)
        #print(file_path)
    #    matching_files.append(file_path)

#print(matching_files)


