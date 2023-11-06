import turtle
import bresenham_algorithm_circle
import sys

bgcolor = 0xffffff
black = 0x000000
fill_color = 0x0000ff # blue

sys.setrecursionlimit(100000) # 재귀 함수 한도를 설정 # 다른 곳에선 사용 X

# 범람 영역 채우기
# 처음엔 Seed 좌표를 정한다(사용자의 마우스 입력등으로 정하기 가능)
# Seed좌표를 기준으로 픽셀을 다른 방향으로 움직여가면서 설정된 background색상과 같다면 fill_color색상으로 바꿔서 영역을 채운다
# 구현은 재귀적으로 구현 가능하며 background색상이 아닌 픽셀을 만나면 재귀함수를 종료한다

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