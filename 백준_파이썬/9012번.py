import sys

def decide():
    line = sys.stdin.readline()
    check = 0
    for i in range(0,len(line)-1):
        if line[i] == '(':
            check+=1
        else: check -=1
        if check < 0:
            break
    if check ==0:
        print("YES")
    else: print("NO")

n = sys.stdin.readline()
n = int(n)

for i in range(0,n):
    decide()
