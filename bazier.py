# bazier curve
import random
import turtle
import math

screen = turtle.Screen()
w, h = 1600, 800

screen.setup(width = w, height = h, startx = 0, starty = 0)
h -= 50
point_minmax = ((-w // 2, w // 2), (-h // 2, h // 2))

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
	if point_count > 6 or point_count < 3:
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

	running = True
	while running:
		if t > 1.0:
			t = 1.0
			running = False

		p02 = [0, 0]
		p02[0] = pow((1 - t), 2) * p0[0] + 2 * t * (1 - t) * p1[0] + pow(t, 2) * p2[0]
		p02[1] = pow((1 - t), 2) * p0[1] + 2 * t * (1 - t) * p1[1] + pow(t, 2) * p2[1]
		point_list.append(p02)

		t += step
	return point_list

def bazier_curve_2d(control_point_list, step):
	if step >= 1.0 or step <= 0.0:
		raise ValueError(f'function bazier_curve_1d: step value error, step value is: {step}\n \
			step value must be (0.0, 1.0)')

	t = 0.0
	point_list = []

	p0 = control_point_list[0]
	p1 = control_point_list[1]
	p2 = control_point_list[2]
	p3 = control_point_list[3]

	running = True
	while running:
		if t > 1.0:
			t = 1.0
			running = False

		p03 = [0, 0]
		p03[0] = pow((1 - t), 3) * p0[0] + 3 * t * pow((1 - t), 2) * p1[0] + 3 * pow(t, 2) * (1 - t) * p2[0] + pow(t, 3) * p3[0]
		p03[1] = pow((1 - t), 3) * p0[1] + 3 * t * pow((1 - t), 2) * p1[1] + 3 * pow(t, 2) * (1 - t) * p2[0] + pow(t, 3) * p3[1]
		point_list.append(p03)

		t += step
	return point_list

def bazier_curve_3d(control_point_list, step):
	if step >= 1.0 or step <= 0.0:
		raise ValueError(f'function bazier_curve_1d: step value error, step value is: {step}\n \
			step value must be (0.0, 1.0)')

	t = 0.0
	point_list = []

	p0 = control_point_list[0]
	p1 = control_point_list[1]
	p2 = control_point_list[2]
	p3 = control_point_list[3]
	p4 = control_point_list[4]

	running = True
	while running:
		if t > 1.0:
			t = 1.0
			running = False

		p04 = [0, 0]
		p04[0] = pow((1 - t), 4) * p0[0] + 4 * t * pow((1 - t), 3) * p1[0] + 6 * pow(t, 2) * pow((1 - t), 2) * p2[0] \
			+ 4 * pow(t, 3) * (1 - t) * p3[0] + pow(t, 4) * p4[0]
		p04[1] = pow((1 - t), 4) * p0[1] + 4 * t * pow((1 - t), 3) * p1[1] + 6 * pow(t, 2) * pow((1 - t), 2) * p2[1] \
			+ 4 * pow(t, 3) * (1 - t) * p3[1] + pow(t, 4) * p4[1]
		point_list.append(p04)

		t += step
	return point_list

def bazier_curve_3d(control_point_list, step):
	if step >= 1.0 or step <= 0.0:
		raise ValueError(f'function bazier_curve_1d: step value error, step value is: {step}\n \
			step value must be (0.0, 1.0)')

	t = 0.0
	point_list = []

	p0 = control_point_list[0]
	p1 = control_point_list[1]
	p2 = control_point_list[2]
	p3 = control_point_list[3]
	p4 = control_point_list[4]
	p5 = control_point_list[5]

	running = True
	while running:
		if t > 1.0:
			t = 1.0
			running = False

		p05 = [0, 0]
		p05[0] = pow((1 - t), 5) * p0[0] + 5 * t * pow((1 - t), 4) * p1[0] + 10 * pow(t, 2) * pow((1 - t), 3) * p2[0] \
			+ 10 * pow(t, 3) * pow((1 - t), 2) * p3[0] + 5 * pow(t, 4) * (1 - t) * p4[0] + pow(t, 5) * p5[0]
		p05[1] = pow((1 - t), 5) * p0[1] + 5 * t * pow((1 - t), 4) * p1[1] + 10 * pow(t, 2) * pow((1 - t), 3) * p2[1] \
			+ 10 * pow(t, 3) * pow((1 - t), 2) * p3[1] + 5 * pow(t, 4) * (1 - t) * p4[0] + pow(t, 5) * p5[1]
		point_list.append(p05)

		t += step
	return point_list


def get_bazier_curve(control_point_list, step):
	length_array = len(control_point_list)
	if length_array < 3 or length_array > 6:
		return None

	point_list = None
	match length_array:
		case 3:
			point_list = bazier_curve_1d(control_point_list, step)
		case 4:
			point_list = bazier_curve_2d(control_point_list, step)
		case 5:
			point_list = bazier_curve_3d(control_point_list, step)
		case 6:
			point_list = bazier_curve_3d(control_point_list, step)

	return point_list



control_point_list = get_random_control_point(6, point_minmax[0], point_minmax[1])

for i in range(len(control_point_list) - 1):
	draw_line_turtle(control_point_list[i], control_point_list[i + 1])

bazier_point_list = get_bazier_curve(control_point_list, 0.01)

turtle.color('blue')
for i in range(len(bazier_point_list) - 1):
	draw_line_turtle(bazier_point_list[i], bazier_point_list[i + 1], False, False)

turtle.exitonclick()