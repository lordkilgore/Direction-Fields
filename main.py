import math, pygame

pygame.display.init()
pygame.font.init()
h = 750
w = 750
win = pygame.display.set_mode((h,w))

# axes
pygame.draw.aaline(win, "white", (0, h / 2), (w, h / 2))
pygame.draw.aaline(win, "white", (w / 2, 0), (w / 2, h))

running = False

# y-prime
def fx (x, y): 
    try:
        return -y/x
    except ZeroDivisionError:
        return 0

# Main
def dg (grid, dx):
    for j in range(columns):
            for i in range(rows):
                starting_point = (math.fabs(-(w / 2) - (transform * (i - (offset_x + dx)))), (h / 2) - (transform * (offset_y + dx - j)))

                x_component = 1 / math.sqrt(((-grid[i][j]) ** 2) + 1)
                y_component = (-grid[i][j]) / math.sqrt(((-grid[i][j]) ** 2) + 1)
                coordinate_transform = [math.fabs(-(w / 2) - (transform * (i - (offset_x - dx)))), (h / 2) - (transform * (offset_y + dx - j))]
                
                ending_point = (coordinate_transform[0] + x_component, coordinate_transform[1] + dy_scalar * y_component)
                
                color_gradient = (255 / rows * i)
                pygame.draw.aaline(win, (color_gradient, 155, 100), starting_point, ending_point)
                pygame.display.flip()
        
    running = True
    while running:
        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

rows, columns = (41, 41)
offset_x = math.floor(rows / 2)
offset_y = math.floor(columns / 2)
transform = 17
dy_scalar = 5
grid = [[0 for i in range(rows)] for j in range(rows)]
for j in range(columns):
    for i in range(rows):
        grid[i][j] = fx(i - offset_x, offset_y - j)

dg(grid, 0.1)
