import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            m1._cells[-1][-1].has_bottom_wall,
            False
        )
    
    def test_reset_cells_visited(self):
        m1 = Maze(0, 0, 10, 10, 10, 10)
        m1._break_entrance_and_exit()
        m1._break_walls_r(0,0)
        m1._reset_cells_visited()
        self.assertEqual(
            m1._cells[5][5]._visited,
            False
        )

    def test_not_reset_cells_visited(self):
        m1 = Maze(0, 0, 10, 10, 10, 10)
        m1._break_entrance_and_exit()
        m1._break_walls_r(0,0)
        #m1._reset_cells_visited()
        self.assertEqual(
            m1._cells[5][5]._visited,
            True
        )



if __name__ == "__main__":
    unittest.main()