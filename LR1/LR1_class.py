import math
import sys
from math import sqrt

class Checker:
    @staticmethod
    def get_coef(index, name):
        try:
            val = float(sys.argv[index])
            print(f"Значение коэффицента {name} успешно считано: {val}")
            return val
        except (IndexError, ValueError): pass

        while True:
            try:
                val = float(input(f"Введите значение коэффицента {name}: "))
                return val
            except ValueError:
                print(f"Коэффицент {name} должен быть целым или вещественным числом.")

class Calculator:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.roots = set()

    def solve_biquad(self):
        if self.a == 0.0:
            print("Данное уравнение не является биквадратным")
            return
        D = self.b**2 - 4 * self.a * self.c

        if D == 0:
            t = -self.b / (2 * self.a)
            self.solve_quad(t)
        elif D > 0:
            t1 = (-self.b -1 * sqrt(D)) / (2 * self.a)
            t2 = (-self.b + 1 * sqrt(D)) / (2 * self.a)
            self.solve_quad(t1, t2)

    def solve_quad(self, *t_vals):
        for t in t_vals:
            if t > 0.0:
                self.roots.update([-sqrt(t), sqrt(t)])
            elif t == 0.0:
                self.roots.add(0.0)

    def sort_roots(self):
        return sorted(list(self.roots))

def main():
    a = Checker.get_coef(1, 'A')
    b = Checker.get_coef(2, 'B')
    c = Checker.get_coef(3, 'C')

    solver = Calculator(a, b, c)
    solver.solve_biquad()

    roots = solver.sort_roots()

    if not roots:
        print("Действительных корней не существует")
    else:
        print(f"Найдено {len(roots)} корней: ", ", ".join(map(str, roots)))
