import sys

n = int(sys.stdin.readline())
office = set()

for i in range(n):
    name, status = sys.stdin.readline().split()
    if status == "enter":
        office.add(name)
    else:
        office.discard(name)

result = sorted(office, reverse=True)

for name in result:
    print(name)