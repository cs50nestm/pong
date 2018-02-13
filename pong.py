# simplePong.py
#
# CS50 AP
# Name: _________________

from graphicsMulti import *
from random import *

# set global variables
HEIGHT = 500
WIDTH = 800
PADHEIGHT = 120
PADWIDTH = 20
RADIUS = 14
WINSCORE = 10

# open window
win = GraphWin("Pong", WIDTH, HEIGHT, autoflush=False)

# TODO
centerLine = Line(Point(WIDTH/2, 0), Point(WIDTH/2, HEIGHT))
centerLine.setWidth(2)
centerLine.draw(win)

def main():

    # TODO
    ball = initBall();
    paddleR = initPaddle(WIDTH - PADWIDTH, "blue")
    paddleL = initPaddle(0, "red")

    # TODO
    dx = randrange(4, 6)
    dy = randrange(-2, 2) + .5

    # TODO
    scoreL = 0
    scoreR = 0
    labelL = initScoreboard(WIDTH / 4)
    labelR = initScoreboard(WIDTH * 3 / 4)

    while True:
        ball.move(dx, dy)

        # TODO
        centerPoint = ball.getCenter()
        x = centerPoint.getX()
        y = centerPoint.getY()

        # TODO
        if y + RADIUS > HEIGHT or y - RADIUS < 0:
            dy = -dy

        # TODO
        yPaddleL = getYPosition(paddleL)
        yPaddleR = getYPosition(paddleR)

        # check which keys are pressed
        keys = win.keysPressed();

        if keys["w"] and yPaddleL > 0:
            paddleL.move(0, -20)
        elif keys["s"] and yPaddleL + PADHEIGHT < HEIGHT:
            paddleL.move(0, 20)

        if keys["o"] and yPaddleR > 0:
            paddleR.move(0, -20)
        elif keys["l"]and yPaddleR + PADHEIGHT  < HEIGHT:
            paddleR.move(0, 20)

        # TODO
        if x + RADIUS >= WIDTH - PADWIDTH and yPaddleR <= y <= yPaddleR + PADHEIGHT:
            dx = -dx

        elif x > WIDTH - PADWIDTH:
            scoreL += 1
            labelL = updateScoreboard(labelL, scoreL)
            ball.undraw()
            win.getMouse()
            ball = initBall()

        # TODO
        if x - RADIUS <= PADWIDTH and yPaddleL <= y <= yPaddleL + PADHEIGHT:
            dx = -dx

        elif x < PADWIDTH:
            scoreR += 1
            labelR = updateScoreboard(labelR, scoreR)
            ball.undraw()
            win.getMouse()
            ball = initBall()

        update()

# TODO
def initBall():
    ball = Circle(Point(WIDTH/2, HEIGHT/2), RADIUS)
    ball.setFill("purple")
    ball.draw(win)
    return ball;

# TODO
def initPaddle(leftpoint, color):
    paddle = Rectangle(Point(leftpoint, HEIGHT/2 - 60), Point(leftpoint + PADWIDTH, HEIGHT/2 + 60))
    paddle.setFill(color)
    paddle.draw(win)
    return paddle

# TODO
def getYPosition(paddle):
    p1 = paddle.getP1()
    p1y = p1.getY()
    return p1y

# TODO
def initScoreboard(position):
    # center label on left
    anchorPoint = Point(position, 50)
    label = Text(anchorPoint, "0")
    label.setSize(36)
    label.setTextColor("Dark Gray")
    label.draw(win)
    return label

# TODO
def updateScoreboard(label, score):
    label.setText(score)
    return label


main()
