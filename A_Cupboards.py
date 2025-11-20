from collections import defaultdict
n = int(input())

left = defaultdict(int,[["0",0],["1",0]])
right = defaultdict(int,[["0",0],["1",0]])


for _ in range(n):
    l,r = input().split()
    left[l] += 1
    right[r] += 1

print(min(list(left.values()))+min(list(right.values())))