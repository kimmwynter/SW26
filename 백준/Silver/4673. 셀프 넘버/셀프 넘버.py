all_numbers = set(range(1, 10001))
generated_numbers = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    generated_numbers.add(i)

self_numbers = sorted(all_numbers - generated_numbers)

for num in self_numbers:
    print(num)