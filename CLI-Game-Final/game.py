# Main file, allows to choose which game to play
import time
import madlibs, adventure, draw # import game files for other games to call them later

def play():
    
    list = "1. Mad Libs\n2. Choose Your Own Adventure\n3. Drawing Game"
    
    print (list)
    
    choice = input("Which game would you like to play? ")
    
    if choice == "1":
        print("-----Loading Mad Libs-----")
        time.sleep(5)
        madlibs.main()
        
    elif choice == "2":
        print("-----Loading Choose Your Own Adventure-----")
        time.sleep(5)
        adventure.main()
    
    elif choice == "3":
        print("Coming Soon")
        print("-----Loading Drawing Game-----")
        time.sleep(5)
        draw.main()
        

if __name__ == "__main__":
    play()