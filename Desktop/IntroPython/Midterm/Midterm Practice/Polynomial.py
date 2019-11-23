def poly(c,x):
    ans = 0
    for n, a in enumerate(c):
        ans += a * x ** n
    return ans




c = [1, 0, 1, 2]
print(poly(c, 2))

b=[1,0,1,0,1]
print(poly(b,4))

d=[1,2,1]
print(poly(d,2))