t1=input().split(" ")
nt,m=int(t1[0]),int(t1[1])
n=0
w,c,dp=[],[],[]
for i in range(nt):
    t2=input().split(" ")
    a,b,v=int(t2[0]),int(t2[1]),int(t2[2])
    if(b<=m):
        for j in range(a):
            w.append(b)
            c.append(v)
            dp.append(0)
        n+=a
'''
for i in range(n):
    print(w[i],c[i])
'''
for i in range(n):
    for v in range(m,0,-1):
        if v>=w[i]:
            dp[v]=max(dp[v],dp[v-w[i]]+c[i])
print(dp[m])
