import sys,math
l = int(sys.argv[1])
def f(n):
    return math.floor(n)
def g(n):
    return math.log2(n)
def c(n,a=0,b=1):
    if n==0:
        return a
    if n==1:
        return b
    return c(n-1,b,a+b)
def t():
    return c(f(g((l**4-l**2)/12))+1)
y=t(l)
def p():
    print(y)