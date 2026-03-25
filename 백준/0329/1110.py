n = int(input())
original_n = n
count = 0

while True:
    ten = n // 10
    one = n % 10
    total = ten + one
    
    n = (one * 10) + (total % 10)
    count += 1
    
    if n == original_n:
        break

print(count)