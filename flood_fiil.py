import turtle
import bresenham_algorithm_circle


bresenham_algorithm_circle.setting_screen()

HW = bresenham_algorithm_circle.HALF_W
HH = bresenham_algorithm_circle.HALF_H

bgcolor = 0xffffff
black = 0x000000
screen_rgb_map = [[bgcolor for _ in range(bresenham_algorithm_circle.H)] for _ in range(bresenham_algorithm_circle.W)]

print(len(screen_rgb_map), len(screen_rgb_map[0]), f'{screen_rgb_map[0][0]:0x}')

circle_points = bresenham_algorithm_circle.draw_circle_bresenham((0 ,0), 100, False)

for point in circle_points:
	for x, y in point:
		screen_rgb_map[x + HW][y + HH] = black

def floor_fill(center, background_color, screen_map):
	cx, cy = center[0], center[1]