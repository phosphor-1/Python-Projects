import game
import turtle, random

def triangle():
    colors = ['red', 'blue', 'green']
    
    t = turtle.Pen()
    
    turtle.bgcolor('black') 
    
    for x in range(360):
        t.pencolor(colors[x%3])
        t.width(x//100+1)
        t.forward(x)
        t.left(119)
    t.bye()
    
    main()    

def square():
    colors = ['red', 'blue', 'green', 'purple']
    
    t = turtle.Pen()
    
    turtle.bgcolor('black') 
    
    for x in range(360):
        t.pencolor(colors[x%4])
        t.width(x//100+1)
        t.forward(x)
        t.left(89)
    t.bye()
    
    main()    

def pentagon():
    colors = ['red', 'blue', 'green', 'purple', 'orange']
    
    t = turtle.Pen()
    
    turtle.bgcolor('black') 
    
    for x in range(360):
        t.pencolor(colors[x%5])
        t.width(x//100+1)
        t.forward(x)
        t.left(71)
    t.bye()

    main()    

def hexagon():
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

    t = turtle.Pen()

    turtle.bgcolor('black')

    for x in range(360):
        t.pencolor(colors[x%6])
        t.width(x//100+1)
        t.forward(x)
        t.left(60)
    t.bye()
    
    main()   
     
def heptagon():
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'cyan']
    
    t = turtle.Pen()
    
    turtle.bgcolor('black') 
    
    for x in range(360):
        t.pencolor(colors[x%7])
        t.width(x//100+1)
        t.forward(x)
        t.left(50.42)
    t.bye()
    
    main()
              
def octagon():
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'cyan', 'lightgreen']
    
    t = turtle.Pen()
    
    turtle.bgcolor('black') 
    
    for x in range(360):
        t.pencolor(colors[x%8])
        t.width(x//100+1)
        t.forward(x)
        t.left(46.5)
    t.bye()
    
    main()    

def randomshape():
    
        randlist = [triangle, square, pentagon, hexagon, heptagon, octagon]
        random.choice(randlist)()  

def main():
    
    print("======================")
    print("== Draw Cool Shapes ==")
    print("======================")
    
    list = "1. Triangle\n2. Square\n3. Pentagon\n4. Hexagon\n5. Heptagon\n6. Octagon\n7.Random!\n8. Return to Main Menu"
    
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
        randomshape()
    elif choose == "8":
        game.play()

if __name__ == "__main__":
    main() 