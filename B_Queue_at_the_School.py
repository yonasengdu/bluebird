n,t = map(int ,input().split())
q = list(input())

while t > 0:
    changes = []
    for i in range(n - 1):
        if q[i] == "B" and q[i + 1] == "G":
            changes.append((i,i+1))
            
    for b, g in changes:
        q[b],q[g] = q[g],q[b]
   
                
               

    t-= 1
            
print("".join(q))
            
    

