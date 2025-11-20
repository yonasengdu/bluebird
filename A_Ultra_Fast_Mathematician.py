a = input()
b = input()

ans = bin(int(a,2)^int(b,2))[2:]
while len(ans) < len(a):
    ans = "0"+ans
    
print(ans)
