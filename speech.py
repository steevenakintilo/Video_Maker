
from gtts import gTTS
import os
from story import *
from image import *

import pyttsx3
from moviepy.editor import *

import numpy as np 

import time

from movie import *
from deep_translator import GoogleTranslator

def translate_word(word):
    to_translate = word

    translated = GoogleTranslator(source='fr', target='en').translate(to_translate)

    return(translated)

def get_right_pic_in_time(word,lst):

    for i in range(len(lst)):
        if word in lst[i]:
            print(lst[i])
            return(lst[i])


def make_video(req):

    debug_test = False
    if debug_test == False:
        if os.path.isdir("images"):
            try:
                os.system("rm -r images")
            except:
                os.system("del -r images")
            print("Remove pic folder")
        else:
            print("Nothing to remove")

        mytext = make_story(req)

        #mytext = "Cette vidéo a été réalisée grâce à une intelligence artificielle et du python.En effet le but de mon compte sera de vous raconter des histoire ou autre sous forme de vidéo généré 100% grâce à une intelligence artificielle et du code.Sous chaque vidéo vous aurez juste à proposer une idée de vidéo et je prendrais l’idée la plus liké pour réaliser la vidéo et la poster sur tiktok."

        print(mytext)
        parse_text = mytext.strip()
        parse_text = parse_text.split(".")

        print(parse_text)
        full_word = []

        for i in range(len(parse_text) - 1):
            time.sleep(10)
            print("Wating 10 secondes")
            full_word.append(make_request_to_ia(parse_text[i]).replace("\n","").replace("\n\n","").replace(".","").replace(",",""))
        
        print(full_word)
        print(len(full_word))
        english_list = []

        for i in range(len(full_word)):
            english_list.append(translate_word(full_word[i]))
        
        print(english_list)
        print("Nombre de mot/imagge = " + str(len(english_list)))
        if len(english_list) < 3:
            print("Not enough word program must restart")
            make_video(res)
        for i in range(len(english_list)):
            make_image(english_list[i])

        language = 'fr'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("story.mp3")
        
    audio = AudioFileClip("story.mp3")

    if mytext != "":
        images = print_full_path_file()
    
    print(images)

    lst_l = []

    for i in range(len(english_list)):
        lst_l.append(get_right_pic_in_time(english_list[i],images))
    
    lst_l = [x for x in lst_l if x is not None]

    audio_len = audio.duration
    video_clips = []
    
    for i in range(len(parse_text) - 1):
        video_clips.append(create_sentence_clip(parse_text[i], lst_l[i]))

    result = concatenate_videoclips(video_clips)
    result = result.set_audio(audio)

    result.write_videofile("output.mp4",fps = 24)

    print("Video done")    