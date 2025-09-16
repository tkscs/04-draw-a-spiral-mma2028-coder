import turtle
from scipy.constants import golden as phi

"""
In a golden spiral, for every 90 degrees, the arm length of the spiral grows
by a factor of phi (which is approximately 1.618)

So if the spiral has so far turned 90 degrees i times, then the current arm
length will be:

initial_arm_length * (phi**i)
"""

### YOUR CODE STARTS HERE
turtle.forward(10)
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(40)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(140)
turtle.right(90)
turtle.forward(230)

### YOUR CODE ENDS HERE

turtle.exitonclick()