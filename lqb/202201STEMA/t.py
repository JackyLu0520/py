t=input().split(' ')
m,n=int(t[0]),int(t[1])
w,c=[0],[0]
for i in range(1,m+1):
    t=input().split(' ')
    w.append(int(t[0]))
    c.append(int(t[1]))
dp=[]
for i in range(0,m+10):
    dp.append(0)
for i in range(1,n+1):
    for v in range(m,0,-1):
        if v-w[i]>=0:
            dp[v]=max(dp[v],dp[v-w[i]]+c[i])
print(dp[m])