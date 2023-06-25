n=int(input())
c=0
for i in range(11,n+1):
    s=str(i)
    for j in range(0,len(s)-1):
        if int(s[j])>int(s[j+1]):
            c-=1;
            break;
    c+=1;
print(c)
