from math import sqrt,ceil

def FindPrimesEratosthenes(n):
    arr = [True] * (n+1)
    
    for i in range(2,ceil(sqrt(n))):
        if arr[i] == True:
            j = i**2
            while  j <= n:
                arr[j] = False
                j += i
    return arr

n,m = map(int,input().split())

primes = FindPrimesEratosthenes(50)
cnt = 0
for i in range(n,m+1):
    if primes[i]:
        cnt+=1
    
if primes[m] and cnt == 2 :
    print("YES")
else:
    print("NO")
                
