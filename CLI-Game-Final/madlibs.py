import time, random, game

print("------------------------------")
print("Mad Libs: Write Your Own Story")
print("------------------------------")

# Story about an Epic Hacker!     
def hackerstory():
        print("Hacker Story")
        name1 = input("Name: ")
        name1prop = name1.capitalize()
        number1 = input("Number: ")
        verb1 = input("Verb: ")
        feds = input("3 Letter Acronym: ")
        bigfeds = feds.upper()
        adj1 = input("Adjective: ")
        place1 = input("Place: ")
        com1 = input("Company Name: ")
        bigcom = com1.upper()  
        adj2 = input("Adjective: ")
        adj3 = input("Adjective: ")
        name2 = input("Name: ")
        name2prop = name2.capitalize()
        adj4 = input("Adjective: ")
        adj5 = input("Adjective: ")
        adj6 = input("Adjective: ")
        verb2 = input("Verb: ")
        noun1 = input("Noun: ")
        adj7 = input("Adjective: ")
        noun2 = input("Noun: ")
        verb3 = input("Verb: ")
        noun3 = input("Noun: ")
        num2 = input("Number: ")
        verb4 = input("Verb: ")
        verb5 = input("Verb: ")
        name3 = input("Name: ")
        name3prop = name3.capitalize()
        noun4 = input("Noun: ")

        #Story Time
        #Gonna print each line on its own
        #Because actual death if I don't

        print("There once was an epic hacker named", name1prop)
        time.sleep(5)
        print("He had pwned over", number1, "machines, and had", verb1, " his way into every Fed computer, even the ones run by The", bigfeds)
        time.sleep(5)
        print("And along his cyber journey,", name1, "decided that it was time to go", adj1, " or go", place1,)
        time.sleep(5)
        print("He decided it was time to go after his biggest target yet:", bigcom,".")
        time.sleep(5)
        print("They were known for having the", adj2, " security, the most", adj3, " employees, and an impenatrable building containg their most secured item:")
        time.sleep(5)
        print(name2prop, "'s Flash Drive")
        time.sleep(5)
        print("This drive contained some of the most",adj4," programs known to man.")
        time.sleep(5)
        print("Big problem though, it was in a very", adj5, " building.")
        time.sleep(5)
        print(name2prop, " knew it would not be", adj6, " to retrieve it, but it had to be done")
        time.sleep(5)
        print("He", verb2, " a plan.")
        time.sleep(5)
        print("First, he would slip the latch on the side door using his trusty", noun1)
        time.sleep(5)
        print("Next, he would look really", adj7, " walking through the building on the lookout for the ", noun2, " room.")
        time.sleep(5)
        print("Lastly, after locating the", noun2, " room, he would figure out the easiest way in")
        time.sleep(5)   
        print("If it had a keypad, he would try to", verb3, " the password from an employee")
        time.sleep(5)
        print("Maybe it's locked with a shitty Kwikset!,", name1prop, " exclaimed.")
        time.sleep(5)
        print("If thats the case, he could use his", noun3, " picks to get past it.")
        time.sleep(5)
        print("He definitely hoped it was a door using HIDProx, so he could test his ESPKey")
        time.sleep(5)
        print("He had to wait", num2, " weeks for it to restock, better make it worth it!")
        time.sleep(5)
        print("Turns out he didnt need any of that.")
        time.sleep(5)
        print(name3prop, ", the head of security, had left the door unlocked!")
        time.sleep(5)
        print("What a", noun4, " of luck!")
        time.sleep(5)
        print("With this", noun4, " of luck, he was able to get the flash drive and leave the facility")
        time.sleep(5)
        print("Unfortunately, he was arrested in the parking lot because he didn't check for cameras and burned his own operation")
        main()

# Story about wilderness survival
def survivalstory():
    print("Survival Story")
    print("Coming Soon!")
    main()

# Spooky Story anyone??
def horrorstory():
        print("Horror Story")
        print("Coming Soon!")
        main()
    
# Alien Story
def scifistory():
        print("Sci Fi Story")
        print("Coming Soon!")
        main()

# Story inspired by a friend :)
def dinosaurstory():
        print("Dinosaur Story")
        print("Coming Soon")
        main()
    
# Uses random.choice to pick a story from a list of functions
def chooserandomstory():
    
        randlist = [hackerstory, survivalstory, horrorstory, scifistory, dinosaurstory]
        random.choice(randlist)()
 
# Where the good stuff is, includes initial list of stories with input
def main():
    while True:    
        list = "1. Hacker Story\n2. Survival Story\n3. Horror Story\n4. Science Fiction Story\n5. Dinosaur Story\n6. I can't decide, choose for me!!!\n7. Exit to Main Menu"

        print(list)
 
        choice = input("Which story would you like to write? ")

        if choice == "1":
            hackerstory()
        
        elif choice == "2":
            survivalstory()
        
        elif choice == "3":
            horrorstory()
        
        elif choice == "4":
            scifistory()
        
        elif choice == "5":
            dinosaurstory()
        
        elif choice == "6":
            chooserandomstory()
        elif choice == "7":
            game.play()

if __name__ == "__main__": 
   main()
  
#i like pie do you like pie yumyuum bebbperfeoif
   