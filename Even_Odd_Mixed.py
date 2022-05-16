n=int(input())
c=0
k=0
e=0
while n:
    d=n%10
    if(d%2==0):
        c+=1
    else:
        k+=1
    n=n//10
    e+=1
if(c==e):
    print('Even')
elif(k==e):
    print('Odd')
else:
    print('Mixed')