import sys
from collections import deque

n = input()
n = int(n)
l1 = deque([])
l2 = deque([])
s1 = []
s2 = []

for i in range(0,n):
    temp = sys.stdin.readline()
    temp = int(temp)
    l1.append(temp)
    l2.append(temp)

num = 1
count = 0
while count != 2*n:
    if num <= n:
        s1.append(num)
        num += 1
        count += 1
    else:
        while len(s1) > 0 and s1[len(s1)-1] == l1[0]:
            l1.popleft()
            s1.pop()
            count+=1
        if len(s1) != 0:
            print("NO")
            exit(0)

    while len(s1) > 0 and s1[len(s1)-1] == l1[0]:
        l1.popleft()
        s1.pop()
        count+=1

num = 1
count = 0
while count != 2*n:
    if num <= n:
        s2.append(num)
        num += 1
        count += 1
        print("+")
    while len(s2) > 0 and s2[len(s2)-1] == l2[0]:
        l2.popleft()
        s2.pop()
        count+=1
        print("-")
