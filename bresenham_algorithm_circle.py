import turtle

W = 1280
H = 800

HALF_W = W // 2
HALF_H = H // 2

turtle.penup() 

screen = turtle.Screen()
screen.setup(width=W, height=H, startx=100, starty=50)

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

turtle.exitonclick()