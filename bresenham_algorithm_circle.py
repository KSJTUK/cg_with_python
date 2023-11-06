import turtle

W = 1280
H = 800

HALF_W = W // 2
HALF_H = H // 2

turtle.penup() 

screen = turtle.Screen()
screen.setup(width=W, height=H, startx=100, starty=50)

turtle.goto(0, HALF_H - 30)
turtle.write(f'formula of circle: if center point is (cx, cy)')
turtle.goto(5 * (len('formula of circle: ') - 1), HALF_H - 45)
turtle.write(f'(x-cx)^2 + (y-cy)^2 = r^2')
turtle.goto(0, HALF_H - 75)
turtle.write(f'polar coordinates: x = cx + r*cos(theta)')
turtle.goto(5 * (len('polar coordinates: ') - 1), HALF_H - 90)
turtle.write('y = cy + r*sin(theta)')

turtle.exitonclick()