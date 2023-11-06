import turtle
import bresenham_algorithm_circle

bgcolor = 0xffffff
black = 0x000000
fill_color = 0x0000ff # blue

def floor_fill(target_point):
	tx, ty = target_point[0], target_point[1]
	if screen_rgb_map[tx][ty] == bgcolor:
		screen_rgb_map[tx][ty] = fill_color
		turtle.goto(tx-HW, ty-HH)
		floor_fill((tx+1, ty))
		floor_fill((tx-1, ty))
		floor_fill((tx, ty+1))
		floor_fill((tx, ty-1))
	else:
		return

def floor_fill_not_recursion(target_point):
	turtle.penup()
	tx, ty = target_point[0], target_point[1]
	while True:
		if screen_rgb_map[tx][ty] == bgcolor:
			screen_rgb_map[tx][ty] = fill_color
			turtle.goto(tx-HW, ty-HH)
			turtle.stamp()

bresenham_algorithm_circle.setting_screen()

HW = bresenham_algorithm_circle.HALF_W
HH = bresenham_algorithm_circle.HALF_H

screen_rgb_map = [[bgcolor for _ in range(bresenham_algorithm_circle.H)] for _ in range(bresenham_algorithm_circle.W)]

print(len(screen_rgb_map), len(screen_rgb_map[0]), f'{screen_rgb_map[0][0]:0x}')

target_point = (0, 0)
circle_points = bresenham_algorithm_circle.draw_circle_bresenham(target_point, 30)

for point in circle_points:
	for x, y in point:
		screen_rgb_map[x + HW][y + HH] = black

turtle.color('blue')
turtle.shape('circle')
turtle.speed(10)
turtle.shapesize(0.1)

turtle.goto(*target_point)
turtle.pendown()
floor_fill((target_point[0]+HW, target_point[1]+HH))

turtle.exitonclick()