import turtle
import random
from sys import float_info
from math import *

# 랜덤한 직선들을 담은 리스트 생성(튜플 내부에 튜플로된 시점, 종점이 존재, Line: (start, end), start:(p1, p2), end(p1, p2) <-이런 형식
def get_random_line_list(list_count, minmax_x, minmax_y):
	rt = [((random.randint(*minmax_x), random.randint(*minmax_y)), (random.randint(*minmax_x), random.randint(*minmax_y))) for _ in range(list_count)]
	return rt

# 터틀 모듈을 사용해서 라인 그리기, 시점 종점에 좌표값을 찍음
def draw_line_turtle(start, end):
	turtle.penup()
	turtle.goto(*start)
	turtle.stamp()
	turtle.write(start)
	turtle.pendown()
	turtle.goto(*end)
	turtle.stamp()
	turtle.write(end)

# 구해진 교점좌표에 새로 점 찍기
def stamp_intersection_point(point, is_print_point = False):
	turtle.penup()
	turtle.goto(*point)
	turtle.stamp()
	if is_print_point:
		turtle.write(tuple(map(lambda x: round(x, 2), point)))

# 교점 좌표 구하기
def get_intersection_point(ap1, ap2, bp1, bp2):
	# 리턴 값이 None이면 교점 존재X
	# under는 나눠줄 값 0이면 교점이 없다 판단하고 None리턴
	under = ((bp2[1] - bp1[1]) * (ap2[0] - ap1[0]) - (bp2[0] - bp1[0]) * (ap2[1] - ap1[1]))
	if fabs(under) < float_info.epsilon:
		return None

	# 교점의 매개 변수 구하기
	# 라인 두개의 매개변수 방정식이 각각 P(t) = (1 - t) * ap1 + t * ap2, P(s) = (1 - s) * bp1 + s * bp2 라고 가정
	_t = ((bp2[0] - bp1[0]) * (ap1[1] - bp1[1]) - (bp2[1] - bp1[1]) * (ap1[0] - bp1[0]))
	_s = ((ap2[0] - ap1[0]) * (ap1[1] - bp1[1]) - (ap2[1] - ap1[1]) * (ap1[0] - bp1[0]))

	# 최종적으로 교점의 매개변수 구하기
	t = _t / under
	s = _s / under

	# 매개변수가 0보다 작거나 1보타 크면 직선위의 점이 아니므로 None리턴
	if (t < 0.0 or t > 1.0 or s < 0.0 or s > 1.0):
		return None
	# 매개변수가 모두 0이면 두 직선은 포함 관계에 있으므로 교점이 무한대로 있음
	# 따라서 교점은 없다고 판단하고 None리턴
	elif fabs(t) < float_info.epsilon and fabs(s) < float_info.epsilon:
		return None

	# 매개 변수를 구하면 교점을 구할 수 있음
	# Px = P1x + t * (P2x - P1x), Py = P1y + t * (P2y - P1y)
	p = (ap1[0] + t * (ap2[0] - ap1[0]), ap1[1] + t * (ap2[1] - ap1[1]))
	return p

line_list = get_random_line_list(30, (-750, 750), (-400, 400))

turtle.color('green')

turtle.shape('circle')
turtle.shapesize(0.3)
for start, end in line_list:
	draw_line_turtle(start, end)

turtle.color('red')

# 라인 마다 검사
# 중복검사 하는 경우가 있어 수정 필요
line_count = len(line_list)
for i in range(line_count):
	line_a = line_list[i]
	for j in range(i, line_count):
		line_b = line_list[j]
		point = get_intersection_point(*line_a, *line_b)
		if point != None:
			stamp_intersection_point(point)

turtle.penup()
turtle.goto(0, 400)
turtle.write("Calc Intersection Point End")
turtle.exitonclick()