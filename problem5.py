sl=list(map(int,input().split()))
n=len(sl)
liss=sorted(sl)
larg=liss[n-2]
small=liss[1]

print(larg+small)
