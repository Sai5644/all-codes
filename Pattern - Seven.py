  1
 12
123


n = int(input())
spaces = n-1
num = 1

for i in range(n):
    for j in range(spaces):
        print(' ',end="")
    for j in range(num):
        print(j+1,end="")
    print()
    spaces = spaces - 1
    num = num + 1
        
    
        
