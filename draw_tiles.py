import turtle

def draw_line(start, end, write_point_coord = True):
	turtle.penup()
	turtle.goto(*start)
	turtle.stamp()
	if write_point_coord: turtle.write(f'{start}')
	turtle.pendown()
	turtle.goto(*end)
	turtle.stamp()
	if write_point_coord: turtle.write(f'{end}')

def draw_rect(lb, rt, write_center = True):
	pass

def draw_coordinates(axis_3d_tuple, step = 10):
	turtle.color('black')
	turtle.penup()
	turtle.goto(0, 0)
	turtle.stamp()
	turtle.write(f'{0, 0}')

	for x in range(-900, 900 + 100, 100):
		if (x == 0):
			continue
		turtle.penup()
		turtle.goto(x, 0)
		turtle.write(f'{(x, 0)}')
		turtle.stamp()
		start = (x, -1080 // 2)
		end = (x, 1080 // 2)
		draw_line(start, end)

	for y in range(-600, 600 + 100, 100):
		if (y == 0):
			continue
		turtle.penup()
		turtle.goto(0, y)
		turtle.write(f'{(0, y)}')
		turtle.stamp()
		start = (-1920 // 2, y)
		end = (1920 // 2, y)
		draw_line(start, end)

turtle.shape('circle')
turtle.shapesize(0.3)

axis = (((-1920 // 2, 0), (1920 // 2, 0)), ((0, -1080 // 2), (0, 1080)))

turtle.color('blue')
draw_line(axis[0][0], axis[0][1])
turtle.color('red')
draw_line(axis[1][0], axis[1][1])

draw_coordinates(axis)


turtle.exitonclick()