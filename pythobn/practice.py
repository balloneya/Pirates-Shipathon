import math
t = int(input())
for i in range(t):
    s, k, m = map(int, input().split())
    gcdOfsk = math.gcd(s, k)
    if m == k:
        if s <= k:
            print(s)
        else:
            print(k-s)
    elif m < k:
        if s <= m:
            print("0")
        else:
            print(s-m)
    else:
        if (m-k) <= k:
            if s <= (m-k):
                print("0")
            elif (s-k) <= (m-k):
                print("0")
