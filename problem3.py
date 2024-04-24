negs=list(map(int,input().split()))
count=0
for i in range(len(negs)):
    if negs[i]<0:
        count+=1
print(count)
