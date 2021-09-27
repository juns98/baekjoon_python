def func(x,y):
    print("<", end='')
    l = []
    for i in range(1, x+1):
        l.append(i)
    index = 0
    len = x
    while len != 0:
        index += y-1
        while index >= len:
            index = index-len
        print(l[index], end='')
        if len != 1:
            print(",", end=' ')
        del l[index]
        len-=1
    print(">", end='')
        



a, b = input().split()
a=int(a)
b=int(b)
func(a,b)
