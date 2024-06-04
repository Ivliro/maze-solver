from graphics import Window,Line,Point
from cell import Cell
from maze import Maze

def main():
    #print('hello world')
    win = Window(800,600)
    # win.draw_line(Line(Point(0,0), Point(50,50)), "black")
    # win.draw_line(Line(Point(0,50), Point(50,0)), "black")
    # win.draw_line(Line(Point(100,0), Point(0,50)), "black")

    # cell1 = Cell(win)
    # cell1.has_right_wall = False
    # cell1.draw(0,0,50,50)
    
    # cell2 = Cell(win)
    # cell2.has_left_wall = False
    # cell2.has_bottom_wall = False
    # cell2.draw(50,0,100,50)

    # cell1.draw_move(cell2)

    # cell3 = Cell(win)
    # cell3.has_top_wall = False
    # cell3.draw(50,150,100,200)

    # cell2.draw_move(cell3,True)

    maze = Maze(0,0,10,10,50,50,win)

    win.wait_for_close()

main()