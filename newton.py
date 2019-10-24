from functions import f1, f2, df1dx1, df1dx2, df2dx1, df2dx2
from gauss import gauss


def jcount1(x1, x2):
    J = [[df1dx1(x1, x2), df1dx2(x1, x2)], [df2dx1(x1, x2), df2dx2(x1, x2)]]
    return J


def jcount2(x1, x2, M):
    J = [[0, 0], [0, 0]]
    dx1 = M * x1
    dx2 = M * x2
    J[0][0] = (f1(x1 + dx1, x2) - f1(x1, x2)) / dx1
    J[0][1] = (f1(x1, x2 + dx2) - f1(x1, x2)) / dx2
    J[1][0] = (f2(x1 + dx1, x2) - f2(x1, x2)) / dx1
    J[1][1] = (f2(x1, x2 + dx2) - f2(x1, x2)) / dx2
    return J


def newton1(x1, x2, NIT, E1, E2):
    print('{:>5}'.format("k"), '{:>15}'.format("d1"), '{:>15}'.format("d2"))
    F = [[0], [0]]
    k = 1
    while k <= NIT:
        F[0] = -f1(x1, x2)
        F[1] = -f2(x1, x2)
        J = jcount1(x1, x2)
        dx = gauss(J, F, 2)
        x1_k = x1 + dx[0]
        x2_k = x2 + dx[1]
        d1 = abs(f1(x1, x2))
        tmp = abs(f2(x1, x2))
        if tmp > d1:
            d1 = tmp
        if x1_k >= 1:
            d2 = abs(x1_k - x1) / x1_k
        else:
            d2 = abs(x1_k - x1)
        if x2_k >= 1:
            tmp = abs(x2_k - x2) / x2_k
        else:
            tmp = abs(x2_k - x2)
        if tmp > d2:
            d2 = tmp
        x1 = x1_k
        x2 = x2_k
        print('{:>5}'.format(k), '{:>15}'.format(format(d1, '.9f')), '{:>15}'.format(format(d2, '.9f')))
        if d1 <= E1 and d2 <= E2:
            break
        if k == NIT:
            exit("IER = 2")
        k += 1
    print("\n")
    return x1, x2


def newton2(x1, x2, NIT, E1, E2, M):
    print('{:>5}'.format("k"), '{:>15}'.format("d1"), '{:>15}'.format("d2"))
    F = [[0], [0]]
    k = 1
    while k <= NIT:
        F[0] = -f1(x1, x2)
        F[1] = -f2(x1, x2)
        J = jcount2(x1, x2, M)
        dx = gauss(J, F, 2)
        x1_k = x1 + dx[0]
        x2_k = x2 + dx[1]
        d1 = abs(f1(x1, x2))
        tmp = abs(f2(x1, x2))
        if tmp > d1:
            d1 = tmp
        if x1_k >= 1:
            d2 = abs(x1_k - x1) / x1_k
        else:
            d2 = abs(x1_k - x1)
        if x2_k >= 1:
            tmp = abs(x2_k - x2) / x2_k
        else:
            tmp = abs(x2_k - x2)
        if tmp > d2:
            d2 = tmp
        x1 = x1_k
        x2 = x2_k
        print('{:>5}'.format(k), '{:>15}'.format(format(d1, '.9f')), '{:>15}'.format(format(d2, '.9f')))
        if d1 <= E1 and d2 <= E2:
            break
        if k == NIT:
            exit("IER = 2")
        k += 1
    print("\n")
    return x1, x2
