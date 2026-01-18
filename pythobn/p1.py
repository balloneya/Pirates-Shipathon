t = int(input())
for i in range(0, t):
    n = int(input())
    if n == 2:
        print("2")
    elif n % 2 == 0:
        print("0")
    elif n % 3 == 0 and n % 2 != 0:
        print("1")
    elif n == 3:
        print("3")
