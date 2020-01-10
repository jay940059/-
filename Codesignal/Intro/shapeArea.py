def shapeArea(n):
    a = 1
    b=0
    for i in range(n-1):
        b = b+a
        a = a+2
    b = b*2+(1+(n-1)*2)
    return b
