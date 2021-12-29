
import sys

n = input()
n = int(n)
movement=[]
lists=[]
temp = sys.stdin.readline()
movement = temp.split()
movement=list(map(int,movement))
for i in range(n):
    j = [i]
    lists.append(j)
for i in range(n):
    lists[i].append(movement[i])


for i in range(n):
    if i == 0:
        index = 0
        move = lists[0][1]
        print(lists[0][0]+1, end=' ')
        if move == n:
            next = 1
        elif move == -n:
            next = 4
        else:
            next = lists[move][0]

        lists.pop(0)
    else:
        for j in range(len(lists)):
            if lists[j][0] == next:
                index = j
                # print("index:", end=' ')
                # print(index)
        for k in range(index):
            lists.append(lists[0])
            lists.pop(0)
        # print(lists)
        print(lists[0][0]+1, end=' ')
        if len(lists) == 1: break
        move = lists[0][1]
        if move >= len(lists):
            move -= 1
            lists.pop(0)
            while move >= len(lists):
                move -= len(lists)
            next = lists[move][0]
        elif move <= -len(lists):
            move += 1
            lists.pop(0)
            move = len(lists)-1+move
            while move <= -len(lists):
                move += len(lists)
            next = lists[move][0]
            # print(next)
        else:
            next = lists[move][0]
            lists.pop(0)


