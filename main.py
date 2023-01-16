from speech import *
import time
import traceback

def main():
    Always = True
    try:
        #make_video("Ecrit une histoire sur un aveugle qui ecoute de la musique")
        make_video(input("Ask me to write a story about whatever you want: "))
    except:
        print(traceback.format_exc())
        pass
    
if __name__ == "__main__":
    time.sleep(1)
    main()