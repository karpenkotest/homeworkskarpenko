filename ='fizzbazz_20.txt'
f = open(filename)
content = f.readlines()
f.close()
for string in content:
  list1 = string.split(" ")
  list_of_numbers=list(map(int,list1))
  print(list_of_numbers)
  counter=1
  for item in list_of_numbers:
      while counter<list_of_numbers[2]+1:
          if not counter%list_of_numbers[0] and not counter%list_of_numbers[1]:
              print("FB")
          elif not counter%list_of_numbers[0] and counter%list_of_numbers[1]:
              print("F")
          elif counter%list_of_numbers[0] and not counter%list_of_numbers[1]:
              print("B")
          else:
               print(counter)
          counter+=1
      print(' ')
          
 