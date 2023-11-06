import turtle

# 원에 대한 브렌즌햄 알고리즘 또한 존재한다
# 원에 대한 브렌즌햄 알고리즘은 원의 방정식을 이용
# 원의 중심이 Cx, Cy 이고 반지름이 r이라고 하면 원의 방정식은
# (x - Cx)^2 + (y - Cy)^2 = r^2 으로 표현된다
# 여기서 (y - Cy)^2 = r^2 - (x - Cx)^2 이다
# 극좌표 식으로 표현하게 되면 x = Cx + r * cos(theta), y = Cy + r * sin(theta)이다

# 원에 대한 브렌즌햄 알고리즘 또한 판별식 p(k)의 부호를 이용하여 x(k+1), y(k+1)을 결정한다
# p(k)를 구하려면 두가지 수식이 필요하다 이를 d1, d2라고 하면
# d1 = y(k)^2 - y^2, d2 = y^2 - (y(k) + 1)^2 이고, (이때 y = r^2 - (x(k) + 1)^2)
# p(k) = d1 - d2 = {y(k)^2 - y^2} - {y^2 - (y(k) + 1)^2} 으로 표현 된다

# 처음 초기화 단계에서
# p1 = y(1)^2 - y^2 - y^2 + (y(k) + 1)^2 (이때 y = r^2 - (x1 + 1)^2)
# x1, y1 = Cx, Cy + r 로 초기화 된다
# k번째 점 x(k), y(k)에 대해서
# 만약 p(k) < 0 이면 x(k+1)=x(k), y(k+1)=y(k)-1 이고 p(k+1) = p(k) + 4 * x(k) + 6
# 만약 p(k) >= 0 이면 x(k+1)=x(k), y(k+1)=y(k) 이고 p(k+1) = p(k) + 4*(x(k) - y(k)) + 10 이다

# 위 k번째 점을 구하는 과정은 x(k) < y(k)일 동안 반복된다 (x(k)가 y(k)보다 커지거나 같아지면 종료)

# 위 과정을 하고나면 원은 1/8영역 그러니까 (Cx, Cy+r)을 기준으로 45도 회전된 만큼만 그려진다
# 45도부터 90도 까지는 y와 x를 swap하면 그릴 수 있고
# 0도부터 90도 까지 즉, 1사분면의 모든 점을 구했으므로 나머지 사분면의 점은 이 점들을
# x,y축에 대해 적절히 반전시키면 원에 대한 모든 점을 구할 수 있다.

def setting_screen():
	global HALF_H, HALF_W, W, H
	W = 1280
	H = 800

	HALF_W = W // 2
	HALF_H = H // 2

	turtle.penup() 

	screen = turtle.Screen()
	screen.setup(width=W, height=H, startx=100, starty=50)

def write_formula():
	global HALF_H, HALF_W
	default_write_x = -50

	next_write_x = default_write_x
	turtle.goto(next_write_x, HALF_H - 30)
	turtle.write(f'formula of circle: if center point is (cx, cy)')
	next_write_x = default_write_x + 5 * (len('formula of circle: ') - 1)
	turtle.goto(next_write_x, HALF_H - 45)
	turtle.write(f'(x-cx)^2 + (y-cy)^2 = r^2')

	next_write_x = default_write_x
	turtle.goto(next_write_x, HALF_H - 75)
	turtle.write(f'polar coordinates: x = cx + r*cos(theta)')

	next_write_x = default_write_x + 5 * (len('polar coordinates: ') - 1)
	turtle.goto(next_write_x, HALF_H - 90)
	turtle.write('y = cy + r*sin(theta)')

	next_write_x = default_write_x + 5 * (len('polar coordinates: x = cx + r*cos(theta)') - 1) + 50
	turtle.goto(next_write_x, HALF_H - 30)
	turtle.write(f'bresenham circle algorithm: while 0 <= theta <= 45 (theta is degree)')
	turtle.goto(next_write_x, HALF_H - 45)
	turtle.write(f'x1=cx, y1=cy+r:')
	turtle.goto(next_write_x, HALF_H - 75)
	turtle.write('assume ({} is assume or define value)')

	next_write_x += 30
	turtle.goto(next_write_x - 5, HALF_H - 90 + 7.5)
	turtle.stamp()
	turtle.goto(next_write_x, HALF_H - 90)
	turtle.write('{ y(k)^2 = r^2 - x(k)^2  =>>  y(k+1)^2 = r^2 - x(k+1)^2 }')

	turtle.goto(next_write_x - 5, HALF_H - 110 + 7.5)
	turtle.stamp()
	turtle.goto(next_write_x, HALF_H - 110)
	turtle.write('{ d1 = y(k)^2 - y^2, d2 = y^2 - (y(k) - 1)^2 }')

	turtle.goto(next_write_x - 5, HALF_H - 130 + 7.5)
	turtle.stamp()
	turtle.goto(next_write_x, HALF_H - 130)
	turtle.write('{y^2 = r^2 - (x(k) + 1)^2}')

	turtle.goto(next_write_x - 5, HALF_H - 150 + 7.5)
	turtle.stamp()
	turtle.goto(next_write_x, HALF_H - 150)
	turtle.write('{ p(k) = d1 - d2 = (y(k)^2 - y^2) - (y^2 - (y(k) - 1)^2)}')

	turtle.goto(next_write_x, HALF_H - 170)
	turtle.write('pseudo code algorithm: assume start point(x1, y1) is (0, r)')
	turtle.goto(next_write_x, HALF_H - 190)
	turtle.write(f'x1: cx, y1: cy + r, p1: 3 - 2r')
	turtle.goto(next_write_x, HALF_H - 210)
	turtle.write('if p(k) < 0 then')
	turtle.goto(next_write_x + 10, HALF_H - 225)
	turtle.write('next point (x(k+1), y(k+1)) is (x(k) + 1, y(k)), p(k+1) = p(k) + 4*x(k) + 6')
	turtle.goto(next_write_x, HALF_H - 240)
	turtle.write('elif 0 <= p(k) then')
	turtle.goto(next_write_x + 10, HALF_H - 255)
	turtle.write('next point (x(k+1), y(k+1)) is (x(k) + 1, y(k)-1), p(k+1) = p(k) + 4*(x(k) - y(k)) + 10')

def swap(a, b):
	a, b = b, a
	return a, b

def draw_circle_bresenham(center_point, radius, draw=True):
	r = radius
	cx, cy = center_point[0], center_point[1]
	x1, y1 = cx, cy + r

	if cy != 0:
		# 2 * cy^2 - 2 * cy * (r + 1)   + 2 * cx^2 + 4 * cx + 3 - 2 * r
		p1 = 2 * cy^2 + 2 * cy * (r + 1) + 2 * cx^2 + 4 * cx + 3 - 2 * r
	else:
		p1 = 3 - 2 * r

	turtle.speed(10)

	turtle.penup()
	turtle.shape('circle')
	turtle.shapesize(0.1)

	turtle.goto(cx, cy)
	turtle.stamp()
	turtle.goto(cx-(5 * (len('center point') // 2)), cy)
	turtle.write(f'center point ({cx}, {cy})')

	p = p1
	x, y = x1, y1

	count = 1
	write_x = -HALF_W + 50
	write_y = HALF_H - 50

	quater_point_list = [(x1, y1)]
	while x < y:
		if p < 0:
			x = x + 1
			y = y
			p = p + 4 * x + 6
		elif p >= 0:
			x = x + 1
			y = y - 1
			p = p + 4 * (x - y) + 10

		quater_point_list.append([x, y])

	quater_point_list += list(map(swap, *zip(*quater_point_list)))
	circle_points = [quater_point_list, list(map(lambda x, y: (x, -y), *zip(*quater_point_list))),
		list(map(lambda x, y: (-x, y), *zip(*quater_point_list))), list(map(lambda x, y: (-x, -y), *zip(*quater_point_list)))]
	if not draw:
		return circle_points

	for points in circle_points:
		for point in points:
			count += 1
			# turtle.goto(write_x, write_y)
			# turtle.write(f'x{count}: {point[0]}, y{count}: {point[1]}')
			# write_y -= 15
			turtle.goto(*point)
			turtle.stamp()

			if count % 50 == 0:
				write_x += 100
				write_y = HALF_H - 50

	return circle_points
if __name__ == '__main__':
	setting_screen()
	write_formula()
	draw_circle_bresenham((0, 0), 90)
	turtle.exitonclick()