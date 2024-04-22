***
 **
  *
n = int(input())
spaces = n-1
stars = 0

for i in range(n):
    for j in range(i):
        print(' ',end="")
    for j in range(stars,n):
        print('*',end="")
    print()
    spaces = spaces - 1
    stars = stars + 1
        
    
        
