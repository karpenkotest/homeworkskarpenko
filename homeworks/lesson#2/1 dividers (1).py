print("Please input integer number and i will show you all dividers :) ")
number=int(input())
range=int(number/2)#  dividers are less than half of the number or divider can be equal to the  half of the number
divider_counter=1
while (divider_counter<=range):
    if not number%divider_counter:
        print(divider_counter)
    divider_counter+=1
print(number)# adding number as own divider
