
from gtts import gTTS
import os
from story import *
from image import *

import pyttsx3
from moviepy.editor import *

import numpy as np 

#lst_l = []

from deep_translator import GoogleTranslator

def translate_word(word):
    to_translate = word

    translated = GoogleTranslator(source='fr', target='en').translate(to_translate)

    return(translated)

def get_right_pic_in_time(word,lst):

    for i in range(len(lst)):
        if word in lst[i]:
            #print(lst[i])
            print(lst[i])
            return(lst[i])
            #lst_l.append(lst[i])

def remove_bad_char(lst):
    l = []

def make_video(req):
    if os.path.isdir("images"):
        os.system("rm -r images")
        print("Remove pic folder")
    else:
        print("Nothing to remove")

    mytext = make_story(req)

    print(mytext)

    parse_text = mytext.strip()
    parse_text = parse_text.split(".")



    #for i in range(len(parse_text)):
    #    print(parse_text[i])
        #print("===")
        #make_request_to_ia(parse_text[i])
    
    #quit()
    l = sum_up_story(mytext)

    
    english_list = []

    for i in range(len(l)):
        english_list.append(translate_word(l[i]))
    
    
    #print(l)

    print(english_list)

    print(len(parse_text))
    print(len(english_list))
    #quit()

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
        #images = print_path_pic()
    
    print(images)

    lst_l = []

    for i in range(len(english_list)):
        lst_l.append(get_right_pic_in_time(english_list[i],images))

    print(lst_l)
    
    lst_l = [x for x in lst_l if x is not None]

    print(len(lst_l))
    audio_len = audio.duration

    print(audio_len)

    f_p_s = audio_len/len(lst_l)

    print(f_p_s)

    lst_l = [np.array(ImageClip(m).get_frame(0)) for m in lst_l]
    clip = ImageSequenceClip(lst_l, fps = 1/f_p_s).crossfadein(1)

    final_clip = clip.set_audio(audio)

    final_clip.write_videofile("video.mp4")

    print("Video Done")
