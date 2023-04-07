from manimlib.imports import *
import numpy as np

# INPUT: отрезок, число точек разбиения, способ выбора оснащения (левые, правые, средние)
# Найдите погрешность оценки, сравните ее с теоретической
#
# погрешностью (формулы выведите с использованием формулы Тейлора с остатком в форме
# Лагранжа). Разбиение равномерное.

class Integral(GraphScene):
    CONFIG={
        "y_max":8,
        "y_axis-height":5
    }

    #define construction of
    def construct(self):
        self.show_function_graph()

    def show_function_graph(self):
        self.setup_axes(animate=True)
        def func(x):
            # our func to integrate
            return 0.1 * (x+ 3 -5) * (x -3-5)* (x-5) + 5

        graph = self.get_graph(func, x_min=0.2, x_max=9)
        graph.set_color(YELLOW)