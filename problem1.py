sum=0
lists=list(map(int,input().split()))
for i in range(len(lists)):
    if lists[i]%2!=0:
        sum+=lists[i]
print(sum)
