# Main file, allows to choose which game to play
import time
import madlibs as ml


def play():
    
    
    list = "1. Mad Libs\n2. Choose Your Own Adventure\n3. Drawing Game"
    
    print (list)
    
    choice = input("Which game would you like to play? ")
    
    if choice == "1":
        print("-----Loading Mad Libs-----")
        time.sleep(5)
        ml.main
        
    elif choice == "2":
        print("Coming Soon!")
    
    elif choice == "3":
        print("Coming Soon")
        

play()