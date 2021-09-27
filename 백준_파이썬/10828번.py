import sys
import re

n = sys.stdin.readline()
n = int(n)
l = []
for i in range(0, n):
    command = sys.stdin.readline()
    if command.find("push") >= 0:
        temp = re.sub(r'[^0-9]', '', command)
        num = int(temp)
        l.append(num)
    elif command.find("pop") >= 0:
        if len(l) > 0:
            print(l[len(l)-1])
            l.pop()
        else: print(-1)
    elif command.find("size") >=0:
        print(len(l))
    elif command.find("empty")>=0:
        if len(l) == 0:
            print(1)
        else: print(0)
    elif command.find("top") >= 0:
        if len(l) > 0:
            print(l[len(l)-1])
        else: print(-1)