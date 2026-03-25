h, m, s = map(int, input().split())
d = int(input())

total_seconds = h * 3600 + m * 60 + s + d

s = total_seconds % 60
total_minutes = total_seconds // 60

m = total_minutes % 60
total_hours = total_minutes // 60

h = total_hours % 24

print(h, m, s)