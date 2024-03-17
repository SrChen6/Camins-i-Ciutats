import unittest
import game
import board
import places

class TestGameFunctions(unittest.TestCase):
    _board = board.Board((6,8), [[5, 8, 9, 2, 5, 4, 3, 6],[1, 4, 2, 5, 7, 7, 9, 2],[5, 8, 9, 2, 5, 4, 3, 6],[1, 4, 2, 5, 7, 7, 9, 2],[5, 8, 9, 2, 5, 4, 3, 6],[1, 4, 2, 5, 7, 7, 9, 2]], [], [])
    print("prints")
    print(_board.size())
    def test_in_board(self):
        self.assertEqual(game._in_board((1,2)), True)

if __name__ == '__main__':
    unittest.main()
