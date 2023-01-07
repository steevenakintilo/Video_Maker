import openai

import os

from decouple import config

def remove_num(s):
    n = "0123456789"
    ss = ""

    for i in range(len(s)):
        if s[i] not in n:
            ss = ss + s[i]
    return(ss)

def make_story(req):

    
    openai.api_key = config('OPEN_IA_KEY')

    model_engine = "text-davinci-003"
    prompt = req

    max_tokens = 128

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return(completion.choices[0].text)


def make_request_to_ia(req):
    openai.api_key = config('OPEN_IA_KEY')

    model_engine = "text-davinci-003"
    prompt = "Ecrit le mot principal de cette phrase" + str(req)

    max_tokens = 128
    w = ""
    word_list = []
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        temperature=0,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    r = completion.choices[0].text
    r_ = r.strip().replace("\n","").replace(".","")
    return (r)
    
def ask_ia_question(req):
    print("")
    openai.api_key = config('OPEN_IA_KEY')

    model_engine = "text-davinci-003"
    prompt = req

    max_tokens = 128
    w = ""
    word_list = []
    
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    r = completion.choices[0].text
    return(r)
