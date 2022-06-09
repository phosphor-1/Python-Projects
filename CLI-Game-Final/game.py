# Main file, allows to choose which game to play
import time
import madlibs, adventure, draw # import game files for other games to call them later

def play():
    
    list = "1. Mad Libs\n2. Choose Your Own Adventure\n3. Drawing Game\n4. Exit Game"
    
    print (list)
    
    choice = input("Which game would you like to play? ")
    
    if choice == "1":
        print("-----Loading Mad Libs-----")
        time.sleep(1)
        for x in range(4):
            print("-----LOADING-----")
            time.sleep(1)
        madlibs.main()
        
    elif choice == "2":
        print("-----Loading Choose Your Own Adventure-----")
        time.sleep(1)
        for x in range(4):
            print("-----LOADING-----")
            time.sleep(1)
        adventure.main()
    
    elif choice == "3":
        print("-----Loading Drawing Game-----")
        time.sleep(1)
        for x in range(4):
            print("-----LOADING-----")
            time.sleep(1)
        draw.main()
    elif choice == "4":
        exit
        

if __name__ == "__main__":
    play()