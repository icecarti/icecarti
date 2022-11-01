import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10
    ) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid = [
            [1, 1, 0, 0, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 1, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 0, 1, 1, 1],
        ]
        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_lines(self) -> None:
        """Отрисовать сетку"""
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def run(self) -> None:
        """Запустить игру"""
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        # Создание списка клеток
        # PUT YOUR CODE HERE

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.draw_lines()

            # Отрисовка списка клеток
            # Выполнение одного шага игры (обновление состояния ячеек)
            # PUT YOUR CODE HERE

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def create_grid(self, randomize: bool = False) -> Grid:
        """
        Создание списка клеток.
        Клетка считается живой, если ее значение равно 1, в противном случае клетка
        считается мертвой, то есть, ее значение равно 0.
        Parameters
        ----------
        randomize : bool
            Если значение истина, то создается матрица, где каждая клетка может
            быть равновероятно живой или мертвой, иначе все клетки создаются мертвыми.
        Returns
        ----------
        out : Grid
            Матрица клеток размером `cell_height` х `cell_width`.
        """
        a = []
        if randomize == True:
            for i in range(self.cell_height):
                row = []
                for j in range(self.cell_width):
                    row.append(random.randint(0, 1))
                a.append(row)
        else:
            for i in range(self.cell_height):
                row = []
                for j in range(self.cell_width):
                    row.append(0)
                a.append(row)

        return a

    def draw_grid(self) -> None:
        """
        Отрисовка списка клеток с закрашиванием их в соответствующе цвета.
        """
        pass

    def get_neighbours(self, cell: Cell) -> Cells:
        """
        Вернуть список соседних клеток для клетки `cell`.
        Соседними считаются клетки по горизонтали, вертикали и диагоналям,
        то есть, во всех направлениях.
        Parameters
        ----------
        cell : Cell
            Клетка, для которой необходимо получить список соседей. Клетка
            представлена кортежем, содержащим ее координаты на игровом поле.
        Returns
        ----------
        out : Cells
            Список соседних клеток.
        """
        if cell[0] == 0:
            #верхняя левая клетка
            if cell[1] == 0:
                return [
                    self.grid[0][1],
                    self.grid[1][0],
                    self.grid[1][1],
                ]
            #верхняя правая клетка
            elif cell[1] == len(self.grid[0]) - 1:
                return [
                    self.grid[0][cell[1] - 1],
                    self.grid[1][cell[1]],
                    self.grid[1][cell[1] - 1],
                ]
            else:
            #остальные клетки в верхней строке
                return [
                    self.grid[0][cell[1] - 1],
                    self.grid[0][cell[1] + 1],
                    self.grid[1][cell[1] - 1],
                    self.grid[1][cell[1] + 1],
                    self.grid[1][cell[1]],
                ]
        elif cell[0] == len(self.grid) - 1:
            #нижняя левая клетка
            if cell[1] == 0:
                return [
                    self.grid[cell[0] - 1][0],
                    self.grid[cell[0] - 1][1],
                    self.grid[cell[0]][1]
                ]
            elif cell[1] == len(self.grid[0]) - 1:
            #нижняя правая клетка
                return [
                    self.grid[cell[0] - 1][cell[1] - 1],
                    self.grid[cell[0]][cell[1] - 1],
                    self.grid[cell[0] - 1][cell[1]],
                ]
            else:
            #остальные клетки в нижней строке
                return [
                    self.grid[cell[0]][cell[1] - 1],
                    self.grid[cell[0] - 1][cell[1] - 1],
                    self.grid[cell[0] - 1][cell[1]],
                    self.grid[cell[0] - 1][cell[1] + 1],
                    self.grid[cell[0]][cell[1] + 1],
                ]
        else:
        #клтеки по правой стороне
            if cell[1] == 0:
                return [
                    self.grid[cell[0] - 1][0],
                    self.grid[cell[0] - 1][1],
                    self.grid[cell[0]][1],
                    self.grid[cell[0] + 1][1],
                    self.grid[cell[0] + 1][0],
                ]
            elif cell[1] == len(self.grid[0]) - 1:
            #клетки по левой стороне
                return [
                    self.grid[cell[0] - 1][cell[1]],
                    self.grid[cell[0] - 1][cell[1] - 1],
                    self.grid[cell[0]][cell[1] - 1],
                    self.grid[cell[0] + 1][cell[1] - 1],
                    self.grid[cell[0] + 1][cell[1]],
                ]
            else:
                return [
                    self.grid[cell[0] - 1][cell[1] - 1],
                    self.grid[cell[0] - 1][cell[1]],
                    self.grid[cell[0] - 1][cell[1] + 1],
                    self.grid[cell[0]][cell[1] + 1],
                    self.grid[cell[0] + 1][cell[1] + 1],
                    self.grid[cell[0] + 1][cell[1]],
                    self.grid[cell[0] + 1][cell[1] - 1],
                    self.grid[cell[0]][cell[1] - 1],
                ]

    def get_next_generation(self) -> Grid:
        """
        Получить следующее поколение клеток.
        Returns
        ----------
        out : Grid
            Новое поколение клеток.
        """
        next_grid = []
        for i in range(self.cell_height):
            row = []
            for j in range(self.cell_width):
                row.append(self.grid[i][j])
            next_grid.append(row)
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if (sum(self.get_neighbours((i, j))) == 2 and self.grid[i][j] == 1) or (sum(self.get_neighbours((i, j))) == 3 and self.grid[i][j] == 1):

                    next_grid[i][j] = 1
                elif sum(self.get_neighbours((i, j))) == 3 and self.grid[i][j] == 0:
                    next_grid[i][j] = 1
                else:
                    next_grid[i][j] = 0

        return next_grid