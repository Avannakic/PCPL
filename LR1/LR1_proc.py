import sys
from math import sqrt

def get_coef(index, name):
    try:
        val = float(sys.argv[index])
        print(f"Значение коэффицента {name} успешно считано: {val}")
        return val
    except (IndexError, ValueError):
        pass

    while True:
        try:
            val = float(input(f"Введите значение коэффицента {name}: "))
            return val
        except ValueError:
            print(f"Коэффицент {name} должен быть целым или вещественным числом")

def solve(a, b, c, roots):
    if a == 0.0:
        print("Данное уравнение не является биквадратным")
        return
    t_roots = []
    D = b ** 2 - 4 * a * c

    if D == 0:
        t = -b / (2 * a)
        t_roots.append(t)
    elif D > 0:
        t1 = (-b - 1 * sqrt(D)) / (2 * a)
        t2 = (-b + 1 * sqrt(D)) / (2 * a)
        t_roots.extend([t1, t2])

    for t in t_roots:
        if t > 0.0:
            roots.update([-sqrt(t), sqrt(t)])
        elif t == 0.0:
            roots.add(0.0)

def main():
    a = get_coef(1, 'A')
    b = get_coef(2, 'B')
    c = get_coef(3, 'C')

    roots = set()
    solve(a, b, c, roots)
    if not roots:
        print("Действительных корней не существует")
    else:
        print(f"Найдено {len(roots)} корней: ", ", ".join(map(str, roots)))
