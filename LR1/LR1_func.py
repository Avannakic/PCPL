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
            print(f"Коэффицент {name} должен быть целым или вещественным числом.")

def get_t_roots(a, b, c):
    if a == 0.0:
        print("Данное уравнение не является биквадратным")
        return ()

    D = b**2 - 4 * a * c

    match D:
        case d if d > 0.0:
            t1 = (-b - 1 * sqrt(D)) / (2 * a)
            t2 = (-b + 1 * sqrt(D)) / (2 * a)
            return (t1, t2)
        case d if d == 0.0:
            t = -b / (2 * a)
            return (t,)
        case _:
            return ()

def get_x_roots(t_roots):
    temp_roots = set()

    for t in t_roots:
        match t:
            case t_val if t_val > 0.0:
                temp_roots.update([-sqrt(t), sqrt(t)])
            case t_val if t_val == 0.0:
                temp_roots.add(0.0)

    return tuple(sorted(temp_roots))

def show_roots(roots):
    match roots:
        case ():
            print("Действительных корней не существует")
        case (r1, ):
            print(f"Один корень: {r1}")
        case (r1, r2):
            print(f"Два корня: {r1}, {r2}")
        case (r1, r2, r3):
            print(f"Три корня: {r1}, {r2}, {r3}")
        case (r1, r2, r3, r4):
            print(f"Четыре корня: {r1}, {r2}, {r3}, {r4}")

def main():
    a = get_coef(1, 'A')
    b = get_coef(2, 'B')
    c = get_coef(3, 'C')
    t_roots = get_t_roots(a, b, c)
    if a == 0.0: return
    x_roots = get_x_roots(t_roots)

    show_roots(x_roots)
