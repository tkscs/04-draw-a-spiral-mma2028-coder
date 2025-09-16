import turtle
from scipy.constants import golden as phi

"""
The aloe polyphylla plant grows in a pattern with five golden spirals
eminating from the same center. Make a function that draws a single golden
spiral, and use that to draw a shape like the aloe polyphylla.

You may find these functions useful:

turtle.up()

turtle.down()

turtle.setposition(x, y)

turtle.setheading(degrees)

The turtle starts at position(0, 0) with heading 0 degrees.
"""

### YOUR CODE STARTS HERE

speed = 0
turtle.speed(speed)
for j in range(5):  
    turtle.up()
    turtle.setposition(0, 0)
    turtle.setheading(j * 72)  
    turtle.down()
    for i in range(100):
        total_degrees_turned_so_far = i * 15
        turtle.forward(phi**(i/6))
        turtle.right(20)

### YOUR CODE ENDS HERE

turtle.exitonclick()