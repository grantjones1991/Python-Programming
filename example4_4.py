# example4_4.py
# code taken from section 4.4 in Python Programming book by John Zelle


from graphics import *
leftEye = Circle(Point(100,100),30)
leftEye.setFill('yellow')
leftEye.setOutline('red')

win = GraphWin()
leftEye.draw(win)

rightEye = leftEye.clone()
rightEye.move(20,0)
rightEye.draw(win)


## This demonstrates how to use the clone method to make an identical object
## if we did leftEye = rightEye, the same object would just have two
## different variable names

newWin = GraphWin()
circ1 = Circle(Point(100,100),30)

circ2 = circ1

circ2.move(20,0)
circ1.draw(newWin)
circ2.draw(newWin)


