"""Created as a solution to an excersize in 
thinkpython by Allen Downey

Written by Brooks Willis

Draws a Dragon curve of given length and given order
"""

from swampy.TurtleWorld import *
from math import *

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def dragonX(t,x,n):
    if n == 0:
        return

    else:	
    	dragonX(t,x,n-1)
    	rt(t,90)
    	dragonY(t,x,n-1)
    	fd(t,x)

def dragonY(t,y,n):
    if n == 0:
    	return

    else:
    	fd(t,y)
    	dragonX(t,y,n-1)
    	lt(t,90)
    	dragonY(t,y,n-1)
    
rt(bob,180)
fd(bob,4)
dragonX(bob,4,10)

wait_for_user()
