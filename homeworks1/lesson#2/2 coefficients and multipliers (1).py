print("Please input integer number and i will show you coefficients and multipliers (decimal system)")
number=int(input())
lenth=len(str(number))
max_degree=lenth-1 
print("Please see coefficients and multipliers")
while max_degree>=0 :
    coefficient=int(number//(10**max_degree))
    print(f"{coefficient}*10**{max_degree}")
    number=number-(coefficient*10**max_degree)
    max_degree-=1
