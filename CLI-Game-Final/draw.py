import game
import turtle


def triangle():
    pass

def square():
    pass

def pentagon():
    pass

def hexagon():
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

    t = turtle.Pen()

    turtle.bgcolor('black')

    for x in range(360):
        t.pencolor(colors[x%6])
        t.width(x//100+1)
        t.forward(x)
        t.left(59)
    
    main()   
     

def heptagon():
    pass

def octagon():
    pass
    

def main():
    
    list = "1. Triangle\n2. Square\n3. Pentagon\n4. Hexagon\n5. Heptagon\n6. Octagon\n7. Return to Main Menu"
    
    print(list)
    
    choose = input("Which Shape would you like to draw? ")
    
    if choose == "1":
        triangle()
    elif choose =="2":
        square()
    elif choose == "3":
        pentagon()
    elif choose == "4":
        hexagon()
    elif choose == "5":
        heptagon()
    elif choose == "6":
        octagon()
    elif choose == "7":
        game.play()

if __name__ == "__main__":
    main() 