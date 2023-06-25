import queue


class node:
    x,y,step=0,0,0
    def __init__(self,_x,_y,_step):
        self.x=_x
        self.y=_y
        self.step=_step
t=input().split(" ")
n,m=int(t[0]),int(t[1])
a,b=[],[]
dirs=[[0,1],[1,0],[0,-1],[-1,0]]
for i in range(n):
    a.append(input().split(' '))
    b.append([0]*m)
t=input().split(' ')
x1,y1,x2,y2=int(t[0]),int(t[1]),int(t[2]),int(t[3])
q=queue.Queue()
q.put(node(x1,y1,0))
f=0
while not q.empty():
    head=q.get()
    for i in range(4):
        tx=head.x+dirs[i][0]
        ty=head.y+dirs[i][1]
        if not b[tx][ty] and not int(a[tx][ty]) and tx>=0 and tx<n and ty>=0 and ty<m:
            b[tx][ty]=1
            q.put(node(tx,ty,head.step+1))
            if tx==x1 and ty==y1:
                f=1
                break
    if f:
        break
if q.empty():
    print(-1)
else:
    print(q.get().step)
        

