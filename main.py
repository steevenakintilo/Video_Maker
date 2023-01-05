from speech import *

def main():
    Always = True
    while Always == True:
        try:
            make_video("Ecrit une histoire sur un sdf qui devient milliardaire")
            Always = False
        except:
            time.sleep(30)
            print("Sleeping a little")
            make_video("Ecrit une histoire sur un sdf qui devient milliardaire")

    
if __name__ == "__main__":
    main()


