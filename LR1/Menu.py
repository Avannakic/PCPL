import sys

import LR1_func
import LR1_proc
import LR1_class

def main():
    while True:
        print("Выберите вариант программы:")
        print("1. ООП-парадигма")
        print("2. Процедурная парадигма")
        print("3. Функциональная парадигма")
        print("0. Завершение")

        choice = input("\nВведите цифру (0-3):").strip()

        match choice:
            case "0":
                print("Завершение работы.")
                sys.exit(0)
            case "1":
                print("\nЗапуск ООП версии")
                LR1_class.main()
            case "2":
                print("\nЗапуск процедурной версии")
                LR1_proc.main()
            case "3":
                print("\nЗапуск функциональной версии")
                LR1_func.main()
            case _:
                print("\nНеизвестная команда")

        if input("\nРешить еще одно уравнение? (y/n): ").strip().lower() != 'y':
            sys.exit(0)

if __name__ == "__main__":
    main()