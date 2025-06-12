n=int(input())
ls=list(map(int,input().split()))
step=0
i=0
while(i<n-1):
		if ls[i]>ls[i+1]:
		    step=step+ls[i] - ls[i+1]
		    ls[i+1]=ls[i]
		i=i+1
print(step)
		
		
