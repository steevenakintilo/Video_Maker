from moviepy.editor import ImageClip, TextClip, CompositeVideoClip


def create_sentence_clip(sentence, picture_path):
  picture = ImageClip(picture_path)
  add_time = 0
  text = TextClip(sentence.strip().replace("\n","").replace("\n\n",""), fontsize=12, color='black',bg_color="white",font="font.ttf")
  
  if len(sentence) < 50:
    add_time = 0.01

    if len(sentence) < 49:
      add_time = add_time - 0.01
    
  
      
  text_duration = len(sentence) * (0.071 + add_time)
  #print(sentence,len(sentence),text_duration)
  picture = picture.set_duration(text_duration)
  text = text.set_duration(text_duration)
  clip = CompositeVideoClip([picture])

  return clip
