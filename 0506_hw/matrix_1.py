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

n = int(input("숫자를 입력하세요.: "))

if 1 < n <= 5:

    matrix_a = make_matrix(n)
    matrix_b = make_matrix(n)
    matrix_c = make_matrix(n)
    
    print_matrix("A", matrix_a)
    print_matrix("B", matrix_b)
    print_matrix("C", matrix_c)

    result = []
    for i in range(n):
        result.append([0] * n)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

            result[i][j] += matrix_c[i][j]

    print_matrix("A * B + C ", result)