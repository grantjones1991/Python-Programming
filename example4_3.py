from graphics import *
# example4_3.py
# This is example code taken from page 90 of the Python Programming textbook by John Zelle



##Open a graphics window
win = GraphWin('Shapes')

# Draw a red circle centered at point (100,100) with radius 30
center = Point(100,100)
cirx = Circle(center, 30)
cirx.setFill('red')
cirx.draw(win)

##Put a textual label in the center of the circle
label = Text(center, "Red Circle")
label.draw(win)

## Draw a square using a rectangle object
Text(Point(100.0, 100.0), 'Red Circle')
rect = Rectangle(Point(30,30),Point(70,70))
rect.draw(win)

## Draw a line segment using a Line object
line = Line(Point(20,30),Point(180, 165))
line.draw(win)

## Draw an ovalusing the Oval object
oval = Oval(Point(20,150), Point(180,199))
oval.draw(win)
