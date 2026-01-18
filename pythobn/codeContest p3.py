import sys
import math
from collections import defaultdict


def solve():
    try:
        n = int(sys.stdin.readline())
        lst = list(map(int, sys.stdin.readline().split()))
    except (ValueError, IndexError):
        return

    if lst.count(0) == 1:
        print("YES")
    elif lst.count(0) >= 2 and lst.count(1) >= 1:
        print("YES")
    else:
        print("NO")


def main():
    try:
        num_test_cases = int(sys.stdin.readline())
    except (ValueError, IndexError):
        num_test_cases = 0

    for _ in range(num_test_cases):
        solve()


if __name__ == "__main__":
    main()
