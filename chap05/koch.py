"""Created as a solution to an excersize in 
thinkpython by Allen Downey

Written by Brooks 

Draws a Koch curve of given length
"""

from swampy.TurtleWorld import *


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def draw(t, length, n):
	if n == 0:
		return
	angle = 50
	fd(t, length*n)
	lt(t, angle)
	draw(t, length, n-1)
	rt(t, 2*angle)
	draw(t, length, n-1)
	lt(t, angle)
	bk(t, length*n)

def koch(t, x):
	"""Draws a Koch curve of length x

	x: Integer, total length of Koch curve
	"""
	if x < 3:
		fd(t, x)
		return
	koch(t, x/3)
	lt(t, 60)
	koch(t, x/3)
	rt(t, 120)
	koch(t, x/3)
	lt(t, 60)
	koch(t, x/3)

def snowflake(t, x):
	"""Draws a snowflake comprised of three koch curves

	x: Integer, length of each component Koch curve
	"""
	for i in range(3):
		koch(t,x)
		rt(t,120)
	
#koch(bob, 200)

length = 200

bob.x = -length/2
bob.y = .3*length

snowflake(bob,length)

wait_for_user()