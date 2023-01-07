from speech import *
import time
import traceback

def main():
    Always = True
    try:
        #make_video("Ecrit une histoire sur un aveugle qui ecoute de la musique")
        make_video("Ecrit une histoire sur un sdf qui habite sur la lune")
    except:
        print(traceback.format_exc())
        pass
    
if __name__ == "__main__":
    time.sleep(1)
    main()