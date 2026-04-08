import sys

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

x.sort()

total_distance = 0
for i in range(n):

    total_distance += x[i] * (2 * i - 2 * (n - 1 - i))

print(abs(total_distance))