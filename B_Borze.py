bronze_encoding= input()
bronze_decoding = []

ptr = 0
n = len(bronze_encoding)

while ptr < n:
    if bronze_encoding[ptr] == ".":
        bronze_decoding.append("0")
        ptr+= 1
        
    elif bronze_encoding[ptr+1] == "-":
        bronze_decoding.append("2")
        ptr+=2
    
    else:
        bronze_decoding.append("1")
        ptr+=2
        
        
print("".join(bronze_decoding))
        
        