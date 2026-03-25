a, b = input().split()

sum_val = int(a, 2) + int(b, 2)
result = bin(sum_val)

print(result[2:])