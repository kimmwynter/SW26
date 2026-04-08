n = int(input())

for i in range(n):
    ox_list = input()
    total_score = 0
    current_streak = 0
    
    for char in ox_list:
        if char == 'O':
            current_streak += 1
            total_score += current_streak
        else:
            current_streak = 0
            
    print(total_score)