n=int(input())
ls=list(map(int,input().split()))
k=(n*(n+1))//2
print(k-sum(ls))