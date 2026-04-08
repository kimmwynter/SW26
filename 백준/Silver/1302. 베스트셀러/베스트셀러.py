import sys

n = int(sys.stdin.readline())
books = {}

for _ in range(n):
    title = sys.stdin.readline().strip()
    if title in books:
        books[title] += 1
    else:
        books[title] = 1

max_count = max(books.values())

best_sellers = []
for title, count in books.items():
    if count == max_count:
        best_sellers.append(title)

best_sellers.sort()
print(best_sellers[0])