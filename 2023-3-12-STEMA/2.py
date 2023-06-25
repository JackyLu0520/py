n=int(input())
ans=10
while n:
    ans=min(ans,n%10)
    n//=10
print(ans)
