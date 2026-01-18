def MEX(list1):
    if not list1:
        return 0

    setOfList = set(list1)
    mex = 0
    while mex in setOfList:
        mex += 1
    return mex


t = int(input())
for i in range(t):
    n = int(input())
    arrayOfNumbers = list(map(int, input().split()))
    isNo = "NO"
    for a in range(n):

    for j in range(n):
        if j != (n-1):
            leftList = arrayOfNumbers[:j+1]
            rightList = arrayOfNumbers[j+1:]
            if MEX(leftList) != MEX(rightList):
                continue
            else:
                isNo = "YES"
        else:
            leftList = arrayOfNumbers[:n]
            rightList = arrayOfNumbers[n-1:]
            if MEX(leftList) != MEX(rightList):
                continue
            else:
                isNo = "YES"
    if isNo == "YES":
        print("NO")
    else:
        print("YES")
