import turtle

W = 1280
H = 800

screen = turtle.Screen()
screen.setup(width=W, height=H, startx=100, starty=100)

screen_rgb_map = [[0 for _ in range(H)] for _ in range(W)]

print(len(screen_rgb_map), len(screen_rgb_map[0]))