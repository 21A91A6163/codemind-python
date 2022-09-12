n=int(input())
for i in range(1,n+1):
    a,b=map(int,input().split())
    t=0
    for j in range(a,b+1):
        k=j%10
        if (k==2 or k==3 or k==9):
            t=t+1
    print(t)