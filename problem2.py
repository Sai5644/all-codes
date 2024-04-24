s=list(map(int,input().split()))
count=0
for i in range(len(s)):
    if s[i]%5==0:
        count+=1
print(count)
