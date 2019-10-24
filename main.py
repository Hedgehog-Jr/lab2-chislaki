from newton import newton1, newton2
from functions import f1, f2


def main():
    x = [[None], [None]]
    print("Решение системы при аналитическом методе: ")
    x = newton1(1, 1, 20, 1e-9, 1e-9)
    print("\tx0 =", x)
    print("Значение 1-ой функции в данной точке: ", format(f1(x[0], x[1]), '.9f'))
    print("Значение 2-ой функции в данной точке: ", format(f2(x[0], x[1]), '.9f'))
    print("\nРешение системы при численном методе: ")
    xM1 = newton2(1, 1, 20, 1e-9, 1e-9, 0.01)
    xM2 = newton2(1, 1, 20, 1e-9, 1e-9, 0.05)
    xM3 = newton2(1, 1, 20, 1e-9, 1e-9, 0.1)
    print("M = 0.01\tx0 =", xM1)
    print("M = 0.05\tx0 =", xM2)
    print("M = 0.10\tx0 =", xM3)
    print("Значение 1-ой функции в данной точке: ", format(f1(xM1[0], xM1[1]), '.9f'))
    print("Значение 2-ой функции в данной точке: ", format(f2(xM1[0], xM1[1]), '.9f'))


main()
