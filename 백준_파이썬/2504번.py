line = input()

stack = []
count = 0
for i in range(len(line)):
    # print(stack)
    if line[i] == '(' or line[i] == '[':
        stack.append(line[i])
    elif line[i] == ')':
        if '(' not in stack:
            print(0)
            exit(0)
        if stack[len(stack)-1] == '(':
            stack.pop(len(stack)-1)
            stack.append(2)
        elif stack[len(stack)-1] == '[' or stack[len(stack)-1] == ')' or stack[len(stack)-1] == ']':
            print(0)
            exit(0)
        else:
            count = 0
            while stack[len(stack) - 1] != '(':
                if stack[len(stack) - 1] != '[':
                    count += stack[len(stack) - 1]
                    stack.pop(len(stack) - 1)
                else:
                    print(0)
                    exit(0)
            stack.pop(len(stack) - 1)
            stack.append(count * 2)
    else:
        if '[' not in stack:
            print(0)
            exit(0)
        if stack[len(stack) - 1] == '[':
            stack.pop(len(stack) - 1)
            stack.append(3)
        elif stack[len(stack)-1] == '(' or stack[len(stack)-1] == ')' or stack[len(stack)-1] == ']':
            print(0)
            exit(0)
        else:
            count = 0
            while stack[len(stack) - 1] != '[':
                if stack[len(stack)-1] != '(':
                    count += stack[len(stack) - 1]
                    stack.pop(len(stack) - 1)
                else:
                    print(0)
                    exit(0)
            stack.pop(len(stack) - 1)
            stack.append(count * 3)
total = 0
for i in range(len(stack)):
    if stack[i] == '(' or stack[i] == '[' or stack[i] == ']' or stack[i] == ')':
        print(0)
        exit(0)
    total += stack[i]

print(total)
