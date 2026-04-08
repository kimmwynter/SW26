import sys

input_data = sys.stdin.read().split()

n = int(input_data[0])
m = int(input_data[1])

unheard = set(input_data[2 : 2 + n])
unseen = set(input_data[2 + n : 2 + n + m])

result = sorted(list(unheard & unseen))

print(len(result))
for name in result:
    print(name)