n=int(input())
l=[]
for i in range(n):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        l.append(i)
m=[]
for i in range(len(l)):
    for j in range(len(l)):
        if i!=j:
            if l[i]*l[j]==n:
                m.append(l[i])
                m.append(l[j])
if(len(m)==0):
    print(-1)
else:
    print(m[0],m[1],end=' ')