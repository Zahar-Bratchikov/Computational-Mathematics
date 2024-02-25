"""
Реализовать методы дихотомии, простых итераций и метод Ньютона для решения нелинейных уравнений
a и b - границы интервала для дихотомии
initial_guess - начальное предположение о корне
tolerance - погрешность
max_iterations - максимальное количество итераций
"""


def f(x):  # Начальная функция
    return x ** 2 - 2


def g(x):  # Эквивалентное выражение
    return (x + 2 / x) / 2


def df(x):  # Производная функции f(x)
    return 2 * x


def bisection_method(a, b, tolerance):
    if f(a) * f(b) > 0:
        print("Нет корня на заданном интервале.")
        return None
    else:
        while (b - a) / 2.0 > tolerance:
            midpoint = (a + b) / 2.0
            if f(midpoint) == 0:
                return midpoint
            elif f(a) * f(midpoint) < 0:
                b = midpoint
            else:
                a = midpoint
        return (a + b) / 2.0


def simple_iteration_method(initial_guess, tolerance, max_iterations):
    x = initial_guess
    iteration = 0
    while iteration < max_iterations:
        x_new = g(x)
        if abs(x_new - x) < tolerance:
            return x_new, iteration
        x = x_new
        iteration += 1
    return None, iteration


def newton_method(f, df, initial_guess, tolerance, max_iterations):
    x = initial_guess
    for _ in range(max_iterations):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tolerance:
            return x_new
        x = x_new
    raise ValueError("Метод Ньютона не сошелся к решению после максимального числа итераций.")


def main():
    initial_guess = 1.5
    tolerance = 1e-6
    max_iterations = 1000
    a = 1
    b = 3
    root_1 = bisection_method(a, b, tolerance)
    print(f"Приближенный корень дихотомией: {root_1:.6f}")
    root_2, iterations_2 = simple_iteration_method(initial_guess, tolerance, max_iterations)
    print(f"Приближенный корень методом простых итераций: {root_2:.6f}")
    root_3 = newton_method(f, df, initial_guess, tolerance, max_iterations)
    print(f"Приближенный корень методом Ньютона: {root_3:.6f}")


if __name__ == "__main__":
    main()
