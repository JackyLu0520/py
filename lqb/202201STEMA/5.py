t=eval(input())
m,n=t[0],t[1];
w=list(eval(input()))
c=list(eval(input()))
w.insert(0,0)
c.insert(0,0)
dp=[]
for i in range(0,m+10):
    dp.append(0)
for i in range(1,n+1):
    for v in range(m,0,-1):
        if v-w[i]>=0:
            dp[v]=max(dp[v],dp[v-w[i]]+c[i])
l=range(11,0,-1)
print(l)
print(dp[m])