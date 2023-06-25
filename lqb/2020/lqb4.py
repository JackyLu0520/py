def gcd(a,b):
    return gcd(b,a%b) if b else a
def lcm(a,b):
    return int(a*b/gcd(a,b))
a=int(input())
b=int(input())
print('%d,%d'%(gcd(a,b),lcm(a,b)))
