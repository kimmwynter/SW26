t = int(input())

for i in range(t):
    vps = input()
    stack = []
    is_vps = True
    
    for char in vps:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                is_vps = False
                break
            stack.pop()
            
    if is_vps and not stack:
        print("YES")
    else:
        print("NO")