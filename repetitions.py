s=input()
res=1
temp=1
for i in range (len(s)-1):
	if s[i+1]==s[i]:
		temp=temp+1
	else:
		res=max(res,temp)
		temp=1
	res=max(res,temp)
print(res)
