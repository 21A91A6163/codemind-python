n=int(input())
for i in range(1,n+1):
    for j in range(1,(n+1)-2):
        print('%d'%j,end='')   
    for j in range(1,n-2):
        print('%d'%j,end='')
    print()
