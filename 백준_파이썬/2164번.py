from collections import deque

n = input()
n = int(n)
d = deque([])

for i in range(0,n):
    d.append(i+1)

while len(d) != 1:
    d.popleft()
    if len(d) == 1: break
    d.append(d[0])
    d.popleft()

print(d[0])
