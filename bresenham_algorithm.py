import turtle
# start = (x1, y1)
# C1 = 2 * delta_y
# C2 = 2 * (delta_y - delta_x)
# p1 = 2 * delta_y - delta_x
# end = (x2, y2)

# if p < 0: 
# 	next_p = p + C1
# elif p >= 0:
# 	next_p = p + C2

W = 1280
H = 800
HALF_W = W // 2
HALF_H = H // 2
screen = turtle.Screen()
turtle.setup(width=W, height=H, startx=100, starty=100)

def draw_line_bresenham(start_point, end_point):
	turtle.penup()
	turtle.speed(10)

	write_w = -HALF_W + 10
	write_h = HALF_H - 50
	x1, y1 = start_point[0], start_point[1]
	x2, y2 = end_point[0], end_point[1]

	delta_x = x2 - x1
	delta_y = y2 - y1

	if delta_y / delta_x > 1:
		return

	C1 = 2 * delta_y
	C2 = 2 * (delta_y - delta_x)
	p1 = 2 * delta_y - delta_x

	turtle.goto(write_w, write_h + 30)
	turtle.write(f'start_point({x1}, {y1}), end_point({x2}, {y2})')
	turtle.goto(write_w + 500, write_h + 30)
	turtle.write(f'formula: if p < 0: next_x = x + 1, next_y = y + 1 and p(n+1) = p(n) + C1')
	turtle.goto(write_w + 500 + 40, write_h + 15)
	turtle.write(f' else if p >= 0: next_x = x + 1, next_y = y and p(n+1) = p(n) + C2')
	turtle.goto(write_w + 500 + 40, write_h - 15)
	turtle.write(f'p1 = 2*delta_y - delta_x, C1 = 2*delta_y, C2 = 2*(delta_y - delta_x)')
	turtle.goto(write_w + 500 + 40, write_h - 30)
	turtle.write(f'delta_y: {delta_y}, delta_x: {delta_x}')
	turtle.goto(write_w + 500 + 40, write_h - 45)
	turtle.write(f'p1 = {p1}, C1 = {C1}, C2 = {C2}')


	count = 1
	p = p1
	x, y = x1, y1
	while True:
		if p < 0:
			p = p + C1
			x += 1
		elif p >= 0 :
			p = p + C2
			x += 1
			y += 1

		turtle.goto(x, y)
		turtle.stamp()
		turtle.goto(write_w, write_h)
		turtle.write(f'x{count:0>3d}: {x:<4d}, y{count:0>3d}: {y:<4d}, p{count:0>3d}: {p:<4d}')

		write_h -= 15
		count += 1

		if count % 50 == 0:
			write_w += 200
			write_h = HALF_H - 50

		if x == x2 and y == y2:
			break

turtle.shape('circle')
turtle.shapesize(0.1)

draw_line_bresenham((1, 1), (100, 97))

turtle.exitonclick()