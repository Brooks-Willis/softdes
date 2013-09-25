"""Created as a solution to an excersize in 
thinkpython by Allen Downey

Written by Brooks Willis

Creates a polygon with any number of sides of any length
or an arc of set set radius and sweep angle
"""

from swampy.TurtleWorld import *
from math import pi

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def lines(bob,length,n,angle):
    """Draws n lines of given length
    
    bob: Turtle
    length: length of each side
    n: number of sides
    angle: angle between segments in degrees
    """
    for i in range(n):
        fd(bob,length)
        lt(bob,angle)


def polygon(t,length,n):
    """Creates a polygon with n sides

    t: Turtle
    length: length of each sides
    n: number of sides
    """
    angle = 360.0/n
    lines(t,length,n,angle)


def square(t,length):
    """Creates a square of variable side length

    t: Turtle
    length: Length of each side
    """
    for i in range(4):
        fd(t,length)
        lt(t)


def arc(t,angle,r):
    """Creates a arc of radius r overa given angle

    t: Turtle
    angle: angle covered by the arc
    r: radius of the arc
    """
    arclength = (2*pi*r*abs(angle))/360
    n = int(arclength/4) +1#number of line segments
    linelength = arclength/n
    lineangle = float(angle)/n

    lines(t,linelength,n,lineangle)

def circle(t,r):
    """Creates a circle of radius r

    t: Turtle
    r: radius of the circle
    """    
    arc(t,360,r)


circle(bob,75)
polygon(bob,100,6)
arc(bob,90,50)

wait_for_user()