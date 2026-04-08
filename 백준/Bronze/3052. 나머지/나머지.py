remainders = []

for i in range(10):
    num = int(input())
    remainders.append(num % 42)

unique_remainders = set(remainders)
print(len(unique_remainders))