import unittest
class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result, "Empty list should return None")

    def test_positive_numbers(self):
        result = max_integer([1, 5, 3, 7, 2])
        self.assertEqual(result, 8)
        
        
def max_integer(list=[]):
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

# print(max_integer([1, 2, 3, 4]))
# print(max_integer([1, 3, 4, 2]))

if __name__ == '__main__':
    unittest.main()

# import sys

# def is_safe(board, row, col, n):
    # Check if there is a queen in the same row
    # if any(board[row][i] == 1 for i in range(col)):
        # return False

    # Check if there is a queen in the upper diagonal on the left side
    # if any(board[i][j] == 1 for i, j in zip(range(row, -1, -1), range(col, -1, -1))):
        # return False

    # Check if there is a queen in the lower diagonal on the left side
    # if any(board[i][j] == 1 for i, j in zip(range(row, n), range(col, -1, -1))):
        # return False

    # return True

# def solve_nqueens_util(board, col, n, solutions):
    # if col == n:
        # solutions.append([[i, j] for i, row in enumerate(board) for j, value in enumerate(row) if value == 1])
        # return

    # for i in range(n):
        # if is_safe(board, i, col, n):
            # board[i][col] = 1
            # solve_nqueens_util(board, col + 1, n, solutions)
            # board[i][col] = 0

# def solve_nqueens(n):
    # if not isinstance(n, int):
        # print("N must be a number")
        # sys.exit(1)

    # if n < 4:
        # print("N must be at least 4")
        # sys.exit(1)

    # board = [[0 for _ in range(n)] for _ in range(n)]
    # solutions = []
    # solve_nqueens_util(board, 0, n, solutions)

    # for solution in solutions:
        # print(solution)

# if __name__ == "__main__":
    # if len(sys.argv) != 2:
        # print("Usage: nqueens N")
        # sys.exit(1)

    # try:
        # N = int(sys.argv[1])
    # except ValueError:
        # print("N must be a number")
        # sys.exit(1)

    # solve_nqueens(N)