"""Дана матрица A размерности n×k и матрица B размерности k×m построить и
вывести матрицу С=A⋅B"""


class KLessThanZero(Exception):
    pass


if __name__ == '__main__':
    with open("input.txt", "r") as input_file:
        try:
            n, k, m = map(int, input_file.readline().split())  # Размерности матриц
            if any(i <= 0 for i in [n, k, m]):
                raise KLessThanZero

            A = [list(map(int, input_file.readline().split())) for i in range(n)]  # Построчно вводится матрица А
            B = [list(map(int, input_file.readline().split())) for i in range(k)]  # Построчно вводится матрица B

            C = [[0] * m for i in range(n)]  # Выходная матрица

            # обработка матриц
            for i in range(n):
                for j in range(m):
                    for r in range(k):
                        C[i][j] += A[i][r] * B[r][j]

            # вывод матрицы в файл
            output_file = open("output.txt", "w", encoding="utf-8")
            for i in range(n):
                output_file.write(" ".join(list(map(str, C[i]))) + "\n")
        except ValueError:
            output_file = open("output.txt", "w", encoding="utf-8")
            output_file.write("Ошибка чтения входных данных.")
        except IndexError:
            output_file = open("output.txt", "w", encoding="utf-8")
            output_file.write("Введена матрица неверного размера.")
        except KLessThanZero:
            output_file = open("output.txt", "w", encoding="utf-8")
            output_file.write("Одна из размерностей меньше либо равна нулю.")

        # Закрытие файлов
        output_file.close()
        input_file.close()

# 5 3 2
# 1 2 3
# 1 2 3
# 2 3 4
# 4 5 6
# 7 8 9
# 2 4
# 2 6
# 8 6

#
# 2 3 3
# 1 2 3
# 1 0 -1
# 3 4 5
# 6 0 -2
# 7 1 8
