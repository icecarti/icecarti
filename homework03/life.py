import pathlib
import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        a = []
        if randomize == True:
            for i in range(self.rows):
                row = []
                for j in range(self.cols):
                    row.append(random.randint(0, 1))
                a.append(row)
        else:
            for i in range(self.rows):
                row = []
                for j in range(self.cols):
                    row.append(0)
                a.append(row)

        return a

    def get_neighbours(self, cell: Cell) -> Cells:
        if cell[0] == 0:
            if cell[1] == 0:
                return [
                    self.curr_generation[0][1],
                    self.curr_generation[1][0],
                    self.curr_generation[1][1],
                ]
            elif cell[1] == self.cols - 1:
                return [
                    self.curr_generation[0][cell[1] - 1],
                    self.curr_generation[1][cell[1] - 1],
                    self.curr_generation[1][cell[1]],
                ]
            else:
                return [
                    self.curr_generation[0][cell[1] - 1],
                    self.curr_generation[1][cell[1] - 1],
                    self.curr_generation[1][cell[1]],
                    self.curr_generation[1][cell[1] + 1],
                    self.curr_generation[0][cell[1] + 1],
                ]
        elif cell[0] == self.rows - 1:
            if cell[1] == 0:
                return [
                    self.curr_generation[cell[0] - 1][0],
                    self.curr_generation[cell[0] - 1][1],
                    self.curr_generation[cell[0]][1],
                ]
            elif cell[1] == self.cols - 1:
                return [
                    self.curr_generation[cell[0] - 1][cell[1] - 1],
                    self.curr_generation[cell[0]][cell[1] - 1],
                    self.curr_generation[cell[0] - 1][cell[1]],
                ]
            else:
                return [
                    self.curr_generation[cell[0]][cell[1] - 1],
                    self.curr_generation[cell[0] - 1][cell[1] - 1],
                    self.curr_generation[cell[0] - 1][cell[1]],
                    self.curr_generation[cell[0] - 1][cell[1] + 1],
                    self.curr_generation[cell[0]][cell[1] + 1],
                ]
        else:
            if cell[1] == 0:
                return [
                    self.curr_generation[cell[0] - 1][0],
                    self.curr_generation[cell[0] - 1][1],
                    self.curr_generation[cell[0]][1],
                    self.curr_generation[cell[0] + 1][1],
                    self.curr_generation[cell[0] + 1][0],
                ]
            elif cell[1] == self.cols - 1:
                return [
                    self.curr_generation[cell[0] - 1][cell[1]],
                    self.curr_generation[cell[0] - 1][cell[1] - 1],
                    self.curr_generation[cell[0]][cell[1] - 1],
                    self.curr_generation[cell[0] + 1][cell[1] - 1],
                    self.curr_generation[cell[0] + 1][cell[1]],
                ]
            else:
                return [
                    self.curr_generation[cell[0] - 1][cell[1] - 1],
                    self.curr_generation[cell[0] - 1][cell[1]],
                    self.curr_generation[cell[0] - 1][cell[1] + 1],
                    self.curr_generation[cell[0]][cell[1] + 1],
                    self.curr_generation[cell[0] + 1][cell[1] + 1],
                    self.curr_generation[cell[0] + 1][cell[1]],
                    self.curr_generation[cell[0] + 1][cell[1] - 1],
                    self.curr_generation[cell[0]][cell[1] - 1],
                ]

    def get_next_generation(self) -> Grid:
        next_grid = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.curr_generation[i][j])
            next_grid.append(row)
        for i in range(self.rows):
            for j in range(self.cols):
                if (sum(self.get_neighbours((i, j))) == 2 and self.curr_generation[i][j] == 1) or (sum(self.get_neighbours((i, j))) == 3 and self.curr_generation[i][j] == 1):
                    next_grid[i][j] = 1
                elif sum(self.get_neighbours((i, j))) == 3 and self.curr_generation[i][j] == 0:
                    next_grid[i][j] = 1
                else:
                    next_grid[i][j] = 0

        return next_grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = self.curr_generation
        self.curr_generation = self.get_next_generation()
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        if self.max_generations is None:
            self.max_generations = 10
        if self.generations >= self.max_generations:
            return True

        return False

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        if self.generations == 20:
            return False
        return True

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        f = open(filename, "r")
        h = sum(1 for line in f)
        f.close()
        f = open(filename, "r")
        x=len(s)
        s = f.readline()
        result = GameOfLife((x, h))
        a = []
        while s != "":
            b = []
            for i in s:
                b.append(ord(i) - ord("0"))
            a.append(b)
            s = f.readline()
        result.curr_generation = a
        return result

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        pass
