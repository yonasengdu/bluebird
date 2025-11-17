n = input()

mx,my,mz = 0,0,0
for n in range(int(n)):
    x,y,z = map(int, input().split())
    mx+= x
    my += y
    mz += z
    
if mx == 0 and my ==0 and mz == 0:
    print("YES")
else:
    print("NO")    
   