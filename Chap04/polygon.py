"""Created as a solution to an excersize in 
thinkpython by Allen Downey

Written by Brooks Willis

Creates a polygon with any number of sides of any length
"""

from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def polygon(bob,length,n):
    """Creates a polygon with n sides

    bob:Turtle
    length: length of each sides
    n: number of sides
    """
    angle = 360.0/n
    for i in range(n):
        fd(bob,length)
        lt(bob,angle)

    print bob

def square(bob,n):
    """Creates a square of variable side length

    bob:Turtle
    length:Length of each side
    """
    for i in range(4):
        fd(bob,n)
        lt(bob)

    print bob

sides = 100 
length = 10

polygon(bob,length,sides)
wait_for_user()