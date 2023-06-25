l=eval(input())
n=eval(input())
Max=-1
for i in range(0,len(l)):
    for j in range(0,len(l)):
        if i!=j and l[i]+l[j]<=n:
            Max=max(Max,l[i]+l[j]);
print(Max)