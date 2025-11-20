n = int(input())
points = list(map(int,input().split()))
lowest = points[0]
highest = points[0]

amazing = 0

prev_point = points[0]
for point in points[1:]:
    if (point > highest and point > prev_point )or \
       (point < lowest and point < prev_point):
        amazing+= 1
        
    lowest = min(lowest,point)
    highest = max(highest,point)
    prev_point = point
    
print(amazing)
        

