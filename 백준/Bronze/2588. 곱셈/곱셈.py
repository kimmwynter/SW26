a = int(input())
b = int(input())

out1 = a * (b % 10)
out2 = a * ((b % 100) // 10)
out3 = a * (b // 100)
out4 = a * b

print(out1)
print(out2)
print(out3)
print(out4)