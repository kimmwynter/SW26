n, k = map(int, input().split())
results = []

for i in range(1, k + 1):
    res = n * i
    reversed_res = int(str(res)[::-1])
    results.append(reversed_res)

print(max(results))