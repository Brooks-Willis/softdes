from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

def square(bob,n):
    for i in range(4):
	    fd(bob,n)
	    lt(bob)

    print bob

square(bob,75)
wait_for_user()