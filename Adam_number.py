n=int(input())
temp=n
rev=0
rev1=0
while n:
    d=n%10
    rev=rev*10+d
    n=n//10
sq=rev*rev
k=sq
while sq:
    d1=sq%10
    rev1=rev1*10+d1
    sq=sq//10
sq1=temp*temp
if sq1==rev1:
    print('True')
else:
    print('False')
    
