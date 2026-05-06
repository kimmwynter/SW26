import random

def print_matrix(name, matrix):
    print(f"--- {name} 행렬 ---")

    for row in matrix:
        for val in row:
            print("{:>7}".format(val), end=" ")
        print()

    print()

def make_matrix(n):
    matrix = []
    limit = n * n * 10

    for i in range(n):
        row = []

        for j in range(n):
            row.append(random.randint(1, limit - 1))

        matrix.append(row)

    return matrix

n = int(input("숫자를 입력하세요: "))

if 1 < n <= 5:

    matrix = make_matrix(n)

    print_matrix("원래 행렬", matrix)

    transpose = []

    for i in range(n):
        transpose.append([0] * n)

    for i in range(n):
        for j in range(n):
            transpose[j][i] = matrix[i][j]

    print_matrix("전치 행렬", transpose)