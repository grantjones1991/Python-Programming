from graphics.zellegraphics import *

'''
bullseye.py
based on Programming exercise 4.2 from Python Programming book by John Zelle
Code written by M. Grant Jones
'''

def main():
    win = GraphWin("Bullseye", 1200, 800)

    white = Circle(Point(600,400),350)
    white.setFill("white")
    white.draw(win)
    c1L = Text(Point(285,400), 1)
    c1L.draw(win)
    c1R = Text(Point(915,400), 1)
    c1R.draw(win)

    black = Circle(Point(600,400),280)
    black.setFill("black")
    black.draw(win)
    c2L = Text(Point(355, 400), 2)
    c2L.setFill("white")
    c2L.draw(win)
    c2R = Text(Point(845, 400), 2)
    c2R.setFill("white")
    c2R.draw(win)

    blue = Circle(Point(600,400),210)
    blue.setFill("blue")
    blue.draw(win)
    c3L = Text(Point(425,400),3)
    c3L.draw(win)
    c3R = Text(Point(775,400),3)
    c3R.draw(win)

    red = Circle(Point(600,400),140)
    red.setFill("red")
    red.draw(win)
    c4L = Text(Point(495,400),4)
    c4L.draw(win)
    c4R = Text(Point(705,400),4)
    c4R.draw(win)

    yellow = Circle(Point(600,400),70)
    yellow.setFill("yellow")
    yellow.draw(win)
    c5 = Text(yellow.getCenter(), 5)
    c5.draw(win)



    message = Text(Point(1100, 110), "Click to quit")
    message.draw(win)
    confirm = win.getMouse()
    win.close()
main()