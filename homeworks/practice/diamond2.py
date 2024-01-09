number=int(input("Enter a number: "))
if  number%2 and number>0:
    print("Be ready to see the diamond")
else:
    print("Please input positive odd number")
center_of_diamond=(number//2)+1
for i in range(center_of_diamond+1):
    print(" "*(center_of_diamond-i),"*"*(2*(i)-1)," "*(center_of_diamond-i))
for i in range(center_of_diamond-1,0,-1):
    print(" "*(center_of_diamond-i),"*"*(2*(i)-1)," "*(center_of_diamond-i))