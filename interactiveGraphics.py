from graphics import *
# interactiveGraphics.py
# Based on programming exercise 4.10.1 from Python Programming book by John Zelle
# Code written by M Grant Jones

def main():
    win = GraphWin()
    shape = Rectangle(Point(50,50), Point(100,100))
    shape.setOutline("red")
    shape.setFill("blue")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        objectCopy = shape.clone()
        objectCopy.draw(win)
        c = objectCopy.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        objectCopy.move(dx,dy)

    message = Text(Point(100,190), "Click to quit")
    message.draw(win)
    confirm = win.getMouse()
    win.close()

main()

# Copy the shape and place it a that place, leaving the previous shape in it's place
