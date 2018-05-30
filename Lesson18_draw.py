import turtle

def draw_square():
	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	steps=1
	while(steps<5):
		brad.forward(100)
		brad.right(90)
		steps+=1

	window.exitonclick()

draw_square()