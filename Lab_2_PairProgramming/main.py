import random
import time


class GameOfLife:
    def __init__(self, rows=3, columns=3):
        self.rows = rows
        self.columns = columns
        self.grid = [[0] * columns for _ in range(rows)]
        for i in range(self.rows):
            for j in range(self.columns):
                self.grid[i][j] = random.choice([0, 1])

    def display(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.grid[i][j] ==1:
                    print("O", end=" ")
                else:
                    print(".", end=" ")
            print("")

    def neighbors(self, x, y):
        neighbors_list = [(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)]
        count = 0

        for i, j in neighbors_list:
            nx = x + i
            ny = y + j

            if 0 <= nx < self.rows and 0 <= ny < self.columns:
                if self.grid[nx][ny] == 1:
                    count += 1

        return count

    def cell_life(self):
        grid_copy = [row[:] for row in self.grid]
        for i in range(self.rows):
            for j in range(self.columns):
                count = self.neighbors(i, j)

                if self.grid[i][j] == 1 and (count < 2 or count > 3):
                    grid_copy[i][j] = 0
                elif self.grid[i][j] == 0 and count == 3:
                    grid_copy[i][j] = 1

        self.grid = grid_copy

    def run(self, iterations=10, delay=1):
        for _ in range(iterations):
            self.display()
            print("")
            self.cell_life()
            time.sleep(delay)

if __name__ == '__main__':
    game = GameOfLife(20, 20)
    game.run()
