import sys


testcase = input()
testcase = int(testcase)


for i in range(testcase):
    temp = sys.stdin.readline()
    nlist = temp.split()
    nlist = list(map(int,nlist))
    numlist = nlist[0]
    target = nlist[1]
    temp = sys.stdin.readline()
    importance = temp.split()
    importance = list(map(int, importance))
   

    count = 0
    while 1:
        check = 0
        for i in range(len(importance)):
            if importance[0] < importance[i]:
                importance.append(importance[0])
                importance.pop(0)
                check = 1
                if target == 0:
                    target = len(importance)-1
                else:
                    target -= 1
                break
        if check == 0:
            if target == 0:
                print(count+1)
                break
            else:
                importance.pop(0)
                count+=1
                target -= 1

