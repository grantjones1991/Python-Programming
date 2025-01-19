#from graphics import *
from graphics.zellegraphics import *


## face.py
## Based off of exercise 4.10.3
## Code written by M Grant Jones

def main():

    print("The code in this program will print out a face in a seperate window.")


###### First window, displays how some objects and points are made. ###################################
    win = GraphWin("Experiemental window", 620,620)    

    message = Text(Point(250,550),"This window displays some tinkering with object and shape objects.")
    message.draw(win)
    p1 = Point(310,10)
    p1.draw(win)
    p2 = Point(550,130)
    p2.draw(win)
    p3 = Point(70,130)
    p3.draw(win)

    apex = Oval(Point(70,10),Point(550,250))
    apex.draw(win)
    
    p4 = Point(520,370)
    p4.draw(win)
    p5 = Point(100,370)
    p5.draw(win)
    p6 = Point(310,550)
    p6.draw(win)
    
    end = Text(Point(550,550),"Click to quit")
    end.draw(win)
    win.getMouse()
    win.close()
#######################################################################################################

###### Second window, displays the face. ###########################################################################
    win = GraphWin("Yo Mom's Face!!!!", 620,620)

    message = Text(Point(300,10),"This window will display a face.  Click to continue after each object is drawn.")
    message.draw(win)
    win.getMouse()

    head = Circle(Point(310,320),300)
    head.draw(win)
    win.getMouse()

    rightEye = Oval(Point(70,130),Point(250,190))
    rightEye.draw(win)
    win.getMouse()

    leftEye = Oval(Point(370,130),Point(550,190))
    leftEye.draw(win)
    win.getMouse()

    rightPupil = Point(160,160)
    rightPupil.draw(win)
    win.getMouse()
    
    leftPupil = Point(460,160)
    leftPupil.draw(win)
    win.getMouse()

    # Nose
    Line(Point(310,190),Point(370,310)).draw(win) #Bridge of nose
    Line(head.getCenter(),Point(370,310)).draw(win) # Bottom of nose
    win.getMouse()

    # Mouth
    Line(Point(160,370),Point(460,370)).draw(win)
    win.getMouse()

    end = Text(Point(550,550),"Click to quit")
    end.draw(win)
    win.getMouse()
    win.close()
#####################################################################################################################
    

main()
