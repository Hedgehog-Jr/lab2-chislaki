def f1(x1, x2):
    return 1.5 * pow(x1, 3) - pow(x2, 2) - 1


def f2(x1, x2):
    return x1 * pow(x2, 3) - x2 - 4


def df1dx1(x1, x2):
    return 4.5 * pow(x1, 2)


def df1dx2(x1, x2):
    return -2 * x2


def df2dx1(x1, x2):
    return pow(x2, 3)


def df2dx2(x1, x2):
    return 3 * x1 * pow(x2, 2)


