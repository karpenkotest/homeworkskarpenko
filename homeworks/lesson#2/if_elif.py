print("Welcome to our cinema. Enter your gender and age and we will help you to select film ")
age=int(input())
genderender=input()
if (age>=18 and genderender=="male"):
    print("Star wars")
elif (age>=18 and genderender=="female"):
  print("50 shades of grey")
elif (age<18 and genderender=="male"):
  print("Ninzyago")
elif (age<18 and genderender=="female"):
  print("The beauty and bist")

