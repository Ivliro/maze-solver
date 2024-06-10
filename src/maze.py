from cell import Cell
import time
import random

class Maze():
    def __init__(
            self,x1,y1,num_rows,num_cols,
            cell_size_x,cell_size_y,win=None,seed=None,
        ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
        if seed is not None:
            self._seed = random.seed(seed)

    def _create_cells(self):
        for i in range(self._num_cols):
            self._cells.append([])
            for j in range(self._num_rows):
                cell = Cell(self._win)
                #cell.draw(x1, y1, x2, y2)
                self._cells[i].append(cell)
                self._draw_cell(i,j)

    def _draw_cell(self,i,j):
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(len(self._cells) - 1, len(self._cells[0]) - 1)

    def _break_walls_r(self,i,j):
        current_cell = self._cells[i][j]
        current_cell._visited = True
        while True:
            cells_to_visit = []
            if i > 0 and not self._cells[i-1][j]._visited:
                cells_to_visit.append((i-1,j))
            if j > 0 and not self._cells[i][j-1]._visited:
                cells_to_visit.append((i,j-1))
            if i < len(self._cells) - 1 and not self._cells[i+1][j]._visited:
                cells_to_visit.append((i+1,j))
            if j < len(self._cells[0]) - 1 and not self._cells[i][j+1]._visited:
                cells_to_visit.append((i,j+1))
            if len(cells_to_visit) == 0:
                self._draw_cell(i,j)
                return
            i2,j2 = random.choice(cells_to_visit)
            # knock down the walls between the current cell and randomly chosen cell
            if i2 == i+1:
                self._cells[i][j].has_right_wall = False
                self._cells[i2][j].has_left_wall = False
            if i2 == i-1:
                self._cells[i][j].has_left_wall = False
                self._cells[i2][j].has_right_wall = False
            if j2 == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j2].has_top_wall = False
            if j2 == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j2].has_bottom_wall = False
            self._break_walls_r(i2,j2)

    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[0])):
                self._cells[i][j]._visited = False