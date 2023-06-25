a=list(eval(input()))
for i in range(len(a)):
    if a[i]<0:
        a[i]*=-1;
a.sort()
for i in range(len(a)-1):
    print(a[i],end=',')
print(a[len(a)-1])
    
