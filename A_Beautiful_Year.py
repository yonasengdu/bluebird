curr_year = int(input())

while True:
    curr_year+=1
    bag = set()
    digits = 0
    temp_year = curr_year
    while temp_year:
        bag.add(temp_year % 10 )
        temp_year //= 10
        digits+=1
        

    if len(bag) == digits:
        break

print(curr_year)
        
            
    
    
    

