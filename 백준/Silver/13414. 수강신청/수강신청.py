import sys

input = sys.stdin.read().split()

k = int(input[0])
l = int(input[1])

waiting_list = {}
for i in range(l):
    student_id = input[i + 2]
    waiting_list[student_id] = i

sorted_list = sorted(waiting_list.items(), key=lambda x: x[1])

count = 0
for student_id, order in sorted_list:
    if count == k:
        break
    print(student_id)
    count += 1