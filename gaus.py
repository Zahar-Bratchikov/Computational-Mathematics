"""
реализовать метод Гауса
A: Матрица коэффициентов уравнений.
B: Матрица свободных членов уравнений.
augmented_matrix: Расширенная матрица, объединяющая матрицы A и B.
n: Количество уравнений (и строк в матрицах A и B).
m: Количество переменных (и столбцов в матрице A).
divisor: Диагональный элемент текущей строки матрицы в прямом ходе метода Гаусса.
factor: Элемент ниже диагонали, используемый для обнуления.
x: Массив для хранения решения системы уравнений.
solution: Решение системы уравнений, возвращаемое функцией gaussian_elimination.
."""

import numpy as np

def gaussian_elimination(A, B):
    augmented_matrix = np.hstack((A, B))
    n, m = augmented_matrix.shape

    print("Начальная расширенная матрица:")
    print(augmented_matrix)
    print()

    for i in range(n):
        divisor = augmented_matrix[i, i]

        augmented_matrix[i, :] /= divisor

        print(f"Шаг {i + 1}: Нормализация {i + 1}-й строки:")
        print(augmented_matrix)
        print()

        for j in range(i + 1, n):
            factor = augmented_matrix[j, i]
            augmented_matrix[j, :] -= factor * augmented_matrix[i, :]

            print(f"Шаг {i + 1}: Обнуление элемента под диагональю в {j + 1}-й строке:")
            print(augmented_matrix)
            print()

    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        x[i] = augmented_matrix[i, -1]

        for j in range(i + 1, n):
            x[i] -= augmented_matrix[i, j] * x[j]

    return x


def main():
    # Ввод пользователем количества уравнений и переменных.
    n = int(input("Введите количество уравнений: "))
    m = int(input("Введите количество переменных: "))

    # Создание и заполнение матрицы коэффициентов A построчно.
    print("Введите матрицу коэффициентов A:")
    A = np.zeros((n, m))
    for i in range(n):
        A[i, :] = list(map(float, input().split()))

    # Создание и заполнение матрицы свободных членов B построчно.
    print("Введите матрицу свободных членов B:")
    B = np.zeros((n, 1))
    for i in range(n):
        B[i, 0] = float(input())

    # Вызов функции gaussian_elimination для решения системы уравнений.
    solution = gaussian_elimination(A, B)

    # Вывод решения системы уравнений.
    print("\nРешение системы:")
    for i, val in enumerate(solution):
        print(f"x{i + 1} =", val)

if __name__ == "__main__":
    main()
