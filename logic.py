"""
    Игра 2048
    Д/з № 3
"""
import random
import numpy as np


class Game:
    """
        Класс описывающий логику и реализацию игры 2048
    """
    def __init__(self):
        """
            Инициализация игры
            Создание пустого поля
        """
        self.score = 0
        self.field = np.array([[0 for col in range(4)]
                               for row in range(4)])

    def swap(self, row, col, route):
        """
            Поменять местами значения в поле в зависимости от type [col, row]
        """
        tmp_value = self.field[row][col]
        self.field[row + route][col] = tmp_value
        self.field[row][col] = 0

    def move_left(self):
        """
            Сдвинуть ячейки влево
        """
        self.field = self.field.transpose()
        for col in range(0, 4):
            while True:
                done = 0
                for row in range(1, 4):
                    if self.field[row][col] != 0:
                        if self.field[row - 1][col] == 0:
                            self.swap(row, col, -1)
                            done += 1
                        elif self.field[row - 1][col] == self.field[row][col]:
                            self.field[row - 1][col] *= 2
                            self.field[row][col] = 0
                            self.score += self.field[row - 1][col]
                            done += 1
                if done == 0:
                    break
        self.field = self.field.transpose()
        return True

    def move_right(self):
        """
            Сдвинуть вправо
        """
        self.field = self.field.transpose()
        for col in range(0, 4):
            while True:
                done = 0
                for row in range(4, 1, -1):
                    row *= -1
                    if self.field[row][col] != 0:
                        if self.field[row + 1][col] == 0:
                            self.swap(row, col, 1)
                            done += 1
                        elif self.field[row + 1][col] == self.field[row][col]:
                            self.field[row + 1][col] *= 2
                            self.field[row][col] = 0
                            self.score += self.field[row + 1][col]
                            done += 1
                if done == 0:
                    break
        self.field = self.field.transpose()
        return True

    def move_up(self):
        """
            Сдвинуть ввевх
        """
        for col in range(0, 4):
            while True:
                done = 0
                for row in range(1, 4):
                    if self.field[row][col] != 0:
                        if self.field[row - 1][col] == 0:
                            self.swap(row, col, -1)
                            done += 1
                        elif self.field[row - 1][col] == self.field[row][col]:
                            self.field[row - 1][col] *= 2
                            self.field[row][col] = 0
                            self.score += self.field[row - 1][col]
                            done += 1
                if done == 0:
                    break
        return True

    def move_down(self):
        """
        Сдвинуть вниз
        """
        for col in range(0, 4):
            while True:
                done = 0
                for row in range(4, 1, -1):
                    row *= -1
                    if self.field[row][col] != 0:
                        if self.field[row + 1][col] == 0:
                            self.swap(row, col, 1)
                            done += 1
                        elif self.field[row + 1][col] == self.field[row][col]:
                            self.field[row + 1][col] *= 2
                            self.field[row][col] = 0
                            self.score += self.field[row + 1][col]
                            done += 1
                if done == 0:
                    break
        return True

    def has_moves(self):
        """
            Выяснить есть ли еще куда ходить
        """
        count = 0
        for row in self.field:
            for cell in row:
                if cell == 0:
                    count += 1
        return count > 0

    def get_score(self):
        """
            Вернуть очки в игре
        """
        return self.score

    def get_field(self):
        """
            Заполнить на поле две случайные ячейки и вернуть поле
        """
        count_cell = 0
        while count_cell < 2 and self.has_moves():
            self.fill_random_cell()
            count_cell += 1
        return self.field

    def fill_random_cell(self):
        row = random.randint(0, 3)
        cell = random.randint(0, 3)
        if self.field[row][cell] == 0:
            if random.randrange(0, 100) <= 10:
                self.field[row][cell] = 4
            else:
                self.field[row][cell] = 2
