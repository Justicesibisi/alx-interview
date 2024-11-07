#!/usr/bin/python3
import sys


def print_solutions(solutions):
    """Prints each solution in the required format."""
    for solution in solutions:
        print(solution)


def solve_nqueens(N):
    """Solves the N Queens problem using backtracking."""
    solutions = []
    board = [-1] * N  # This will store the column index for queens in each row

    def is_safe(row, col):
        """Checks if it's safe to place a queen at (row, col)."""
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def backtrack(row):
        """Backtracks to find all solutions."""
        if row == N:
            # All queens are placed, add this solution
            solutions.append([[r, board[r]] for r in range(N)])
            return

        for col in range(N):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # Reset

    backtrack(0)
    return solutions


def main():
    """Main function to handle user input and solve the problem."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
