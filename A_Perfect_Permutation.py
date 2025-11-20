n = int(input())

if n % 2 :
    print(-1)
    
else:
    ans = [i for i in range(1,n+1)]
    for i in range(1,n,2):
        ans[i-1],ans[i] = ans[i],ans[i-1]
    print(*ans)