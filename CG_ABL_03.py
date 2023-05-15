import pygame

# define region codes
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

# define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

def compute_region_code(x, y, xmin, ymin, xmax, ymax):
    """
    Compute the region code of a point with respect to a clipping window
    """
    code = INSIDE
    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP
    return code

def cohen_sutherland(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    """
    Clip a line segment to a rectangular clipping window using the Cohen-Sutherland algorithm
    """
    # compute region codes for the endpoints of the line segment
    code1 = compute_region_code(x1, y1, xmin, ymin, xmax, ymax)
    code2 = compute_region_code(x2, y2, xmin, ymin, xmax, ymax)

    while True:
        # if both endpoints are inside the clipping window, accept the line segment
        if code1 == INSIDE and code2 == INSIDE:
            return x1, y1, x2, y2

        # if both endpoints share an outside region, reject the line segment
        if code1 & code2 != 0:
            return None

        # otherwise, compute the intersection of the line segment with the clipping window
        code = code1 if code1 != INSIDE else code2
        if code & TOP:
            x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
            y = ymax
        elif code & BOTTOM:
            x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
            y = ymin
        elif code & RIGHT:
            y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
            x = xmax
        elif code & LEFT:
            y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
            x = xmin

        # update the endpoint that is outside the clipping window
        if code == code1:
            x1, y1 = x, y
            code1 = compute_region_code(x1, y1, xmin, ymin, xmax, ymax)
        else:
            x2, y2 = x, y
            code2 = compute_region_code(x2, y2, xmin, ymin, xmax, ymax)

def draw_line(screen, color, x1, y1, x2, y2):
    """
    Draw a line on the Pygame screen
    """
    pygame.draw.line(screen, color, (x1, y1), (x2, y2), 2)

def main():
    # initialize Pygame
    pygame.init()

    # set up the window
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Cohen-Sutherland Algorithm")

