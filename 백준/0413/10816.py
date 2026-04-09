import sys
from collections import Counter

input = sys.stdin.read().split()

n = int(input[0])
sanggeun_cards = input[1 : n+1]

m = int(input[n+1])
targets = input[n+2 : n+2+m]

count_map = Counter(sanggeun_cards)

result = []
for target in targets:
    result.append(str(count_map[target]))

print(" ".join(result))