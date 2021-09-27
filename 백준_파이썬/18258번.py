import sys
from collections import deque

n = sys.stdin.readline()
n = int(n)
l = deque([])
length = 0
index = 0
for i in range(0, n):
    command = sys.stdin.readline().strip()
    if command == "pop":
        if len(l) > 0:
            print(l[0])
            l.popleft()
        else: print(-1)
    elif command == "size":
        print(len(l))
    elif command == "empty":
        if len(l) == 0:
            print(1)
        else: print(0)
    elif command == "front":
        if len(l) > 0:
            print(l[0])
        else: print(-1)
    elif command == "back":
        if len(l) > 0:
            print(l[len(l)-1])
        else: print(-1)
    else:
        list = command.split()
        num = int(list[1])
        l.append(num)