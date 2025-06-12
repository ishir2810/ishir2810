n=int(input())
if n==1:
	print(1)
elif n<4:
    print('NO SOLUTION')
elif n==4:
    print(3,' ',1,' ',4,' ',2)
else:
    ls=['3','1','4','2']
    beg=[]
    end=[]
    i=5
    while(i<=n):
        if i&1==0:
            end.append(str(i)) 
        else:
            beg.append(str(i)) 
        i=i+1
    if not end:
        res=beg+ls
        print(' '.join(res))
    else:
        res=beg+ls+end
        print(' '.join(res))
