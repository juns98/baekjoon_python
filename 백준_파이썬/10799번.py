import sys

n = sys.stdin.readline()
stack=[]

total = 0
laser = 1
count = 0
check = 1
laser = 0
board = 0

for i in range(len(n)):
    # if n[i] == '(':
    #     stack.append(n[i])
    # else:
    #     if stack[-1] == '(':
    #         stack.pop()
    #         stack.append('1')
    #     else:
    #         j=0
    #         while j != len(stack):
    #             if stack[-1-j] == '1':
    #                 count+=1
    #                 j+=1
    #             else:
    #                 total += count+1
    #                 stack.pop(-1-j)
    #                 count = 0
    #                 break
    if n[i] == '(':
        stack.append(n[i])
        board+=1
    else:
        if stack[-1] == '(':
            stack.pop()
            stack.append('1')
            board -= 1
            total += board
        else:
            total+=1
            board -= 1
print(total-1)
                                   