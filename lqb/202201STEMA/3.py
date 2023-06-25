s=input()
l=len(s)
n=eval(s)
if n*n%(10**l)==n:
    print('Y')
else:
    print('N')