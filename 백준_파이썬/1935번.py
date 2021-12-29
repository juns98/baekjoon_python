n = input()
n = int(n)
list = []
stack=[]
line = input()
linelist=[]
for i in range(n):
    k = input()
    k = int(k)
    list.append(k)

for i in range(len(line)):
    linelist.append(line[i])
while len(linelist) > 0:
    if ord(linelist[0]) >= 65 and ord(linelist[0]) <= 90 :
        temp = ord(linelist[0])-65
        stack.append(list[temp])
        linelist.pop(0)
    else:
        if linelist[0] == '+':
            temp = stack[-1] + stack[-2]
            stack.pop()
            stack.pop()
            stack.append(temp)
        elif linelist[0] == '-':
            temp = stack[-2] - stack[-1]
            stack.pop()
            stack.pop()
            stack.append(temp)
        elif linelist[0] == '*':
            temp = stack[-2] * stack[-1]
            stack.pop()
            stack.pop()
            stack.append(temp)
        elif linelist[0] == '/':
            temp = stack[-2] / stack[-1]
            stack.pop()
            stack.pop()
            stack.append(temp)
        linelist.pop(0)

stack[0] = float(stack[0])
print("{:.2f}".format(stack[0]))
