import math
t = int(input())
for i in range(0, t):
    n, x = map(int, input().split())
    arrayGiven = list(map(int, input().split()))
    if n == x:
        print(n)
    elif x == 0:
        for i in range(0, n+1):
            if i not in arrayGiven:
                print(i)
                break
            else:
                continue
    else:
        maxElement = max(arrayGiven)
        minElement = min(arrayGiven)
        if maxElement == n and minElement == 0:
            print(n)
        else:
            countOfMinElement = 0
            countOfMaxElement = 0
            for i in arrayGiven:
                if i == minElement:
                    countOfMinElement += 1
                elif i == maxElement:
                    countOfMaxElement += 1
            if maxElement == n:
                if countOfMaxElement == 1:
                    print(n)
                elif countOfMaxElement == x:
                    print(n)
                elif minElement == 1:
                    print("2")
                else:
                    print(minElement-1)
            elif minElement == 0:
