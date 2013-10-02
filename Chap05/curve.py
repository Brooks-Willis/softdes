"""Created as a solution to an excersize in 
thinkpython by Allen Downey

Written by Brooks Willis

Draws a Gosper curve of given length
"""

from swampy.TurtleWorld import *
from math import *

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def gosperA(t,length):
    if length >=20:
    	gosperA(t,length/4)
    	lt(t,60)
    	gosperB(t,length/4)
    	lt(t,120)
    	gosperB(t,length/4)
    	rt(t,60)
    	gosperA(t,length/4)
    	rt(t,120)
    	gosperA(t,length/4)
    	gosperA(t,length/4)
    	rt(t,60)
    	gosperB(t,length/4)
    	lt(t,60)
    else:
    	fd(t,length)

def gosperB(t,length):
    if length >=20:
        rt(t,60)
        gosperA(t,length/4)
        lt(t,60)
        gosperB(t,length/4)	
        gosperB(t,length/4)
        lt(t,120)
        gosperB(t,length/4)
        lt(t,60)
        gosperA(t,length/4)
        rt(t,120)
        gosperA(t,length/4)
        rt(t,60)
        gosperB(t,length/4)
    else:
        fd(t,length)   

gosperA(bob,1000)
wait_for_user()