n = int(input())
orange_in_drinks = list(map(int,input().split()))
orange_in_cocktail = 0
for orange_in_drink in orange_in_drinks:
    orange_in_cocktail += orange_in_drink*(1/n) 
    
print(orange_in_cocktail)