fizz=int(input('Input Fizz:'))
buzz=int(input("Input Buzz:"))
random_number=int(input("Random number:"))
i=1
for i in range(1,random_number+1):
    if i%fizz and i%buzz:
            print(i,end=''" ")
    elif not i%(fizz*buzz):
        print("FB",end=''  " ")
    elif not i%fizz and i%buzz:
      print("F",end=''  " ")
    elif i%fizz and  not i%buzz:
        print("B",end=''" ")


