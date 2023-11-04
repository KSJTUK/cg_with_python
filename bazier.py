# bazier curve
import random
import turtle
import math

# 터틀 모듈을 사용해서 라인 그리기, 시점 종점에 좌표값을 찍음
def draw_line_turtle(start, end, print_point = True, draw_stamp = True):
	turtle.penup()
	turtle.goto(*start)
	if draw_stamp:
		turtle.stamp()
	if print_point:
		turtle.write(start)
	turtle.pendown()
	turtle.goto(*end)
	if draw_stamp:
		turtle.stamp()
	if print_point:		
		turtle.write(end)

def get_random_control_point(point_count, minmaxX, minmaxY):
	if point_count > 5 or point_count < 3:
		return None
	return [(random.randint(*minmaxX), random.randint(*minmaxY)) for _ in range(point_count)]
	
def bazier_curve_1d(control_point_list, step):
	if step >= 1.0 or step <= 0.0:
		raise ValueError(f'function bazier_curve_1d: step value error, step value is: {step}\n \
			step value must be (0.0, 1.0)')

	t = 0.0
	point_list = []

	p0 = control_point_list[0]
	p1 = control_point_list[1]
	p2 = control_point_list[2]
	while True:
		if t > 1.0:
			break

		p02 = [0, 0]
		p02[0] = pow((1 - t), 2) * p0[0] + 2 * t * (1 - t) * p1[0] + pow(t, 2) * p2[0]
		p02[1] = pow((1 - t), 2) * p0[1] + 2 * t * (1 - t) * p1[1] + pow(t, 2) * p2[1]
		point_list.append(p02)

		t += step
	return point_list

control_point_list = get_random_control_point(3, (-100, 100), (-100, 100))

for i in range(len(control_point_list) - 1):
	draw_line_turtle(control_point_list[i], control_point_list[i + 1])

bazier_point_list = bazier_curve_1d(control_point_list, 0.5)
for i in range(len(bazier_point_list) - 1):
	draw_line_turtle(bazier_point_list[i], bazier_point_list[i + 1], False, False)

turtle.exitonclick()