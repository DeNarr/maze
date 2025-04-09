from graphics import *


def main():
    win = Window(800, 600)
    point1 = Point(20, 20)
    point2 = Point(270, 70)
    line = Line(point1, point2)
    win.draw_line(line, "black")
    line2 = Line(Point(50, 50), Point(400, 400))
    win.draw_line(line2, "red")
    win.wait_for_close()


main()
