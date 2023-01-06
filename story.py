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

    # Set the model and prompt
    model_engine = "text-davinci-003"
    prompt = req

    # Set the maximum number of tokens to generate in the response
    max_tokens = 128

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Print the response
    return(completion.choices[0].text)


def sum_up_story_(text):
    openai.api_key = config('OPEN_IA_KEY')
    model_engine = "text-davinci-003"
    prompt = "Ecrit le mot le plus important de chaque phrase du texte: " + "\n" + text.replace("\n","").strip()

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
    lines = r.split('\n')
    words = []
    words_ = []
    all_word = []
    for line in lines:
        parts = line.split('/')
        if parts != '':
            words.extend(parts)
    
    for i in range(len(words)):
        if words[i] != "" and words[i].replace(".","").isnumeric() == False:
            words_.append(words[i])
    
    for i in range(len(words_)):
        wo = words_[i].split(",")
        for j in range(len(wo)):
            all_word.append(remove_num(wo[j]))

    print(all_word)
    return (all_word)


def make_request_to_ia(req):
    print("")
    openai.api_key = config('OPEN_IA_KEY')

    # Set the model and prompt
    model_engine = "text-davinci-003"
    prompt = "Ecrit le mot principal de cette phrase" + str(req)

    # Set the maximum number of tokens to generate in the response
    max_tokens = 128
    w = ""
    word_list = []
    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        temperature=0,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Print the response
    r = completion.choices[0].text
    r_ = r.strip().replace("\n","").replace(".","")
    #print("mot = " + r)
    return (r)
    
def sum_up_story(text):
    print("")
    openai.api_key = config('OPEN_IA_KEY')

    # Set the model and prompt
    model_engine = "text-davinci-003"
    prompt = "Quels sont les 10 mots principaux de ce texte: " + "\n" + text

    # Set the maximum number of tokens to generate in the response
    max_tokens = 128
    w = ""
    word_list = []
    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Print the response
    r = completion.choices[0].text
    #print(r)
    r = r.split("\n")


    for i in range(len(r)):
        l = r[i].split(".")
        if "." in r[i]:
            word_list.append(l[1].strip())
    print(word_list)
    #print(type(word_list))
    return(word_list)

