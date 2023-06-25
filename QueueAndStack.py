class stack:
    def __init__(self):
        self.data=[]
        self.top=0
    def push(self,x):
        self.data.append(x)
        self.top+=1
    def pop(self):
        if top==0:
            return "underflow"
        else:
            self.top-=1
            return self.data[top+1]
class queue:
    def __init__(self):
        self.data=[]
        self.head=0
        self.tail=0
    def ins(self,x):
        self.data.append(x)
        self.tail+=1
    def delete(self):
        if head==tail:
            return "empty queue"
        else:
            self.head+=1
            return self.data[head-1]
    