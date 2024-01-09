filename ='fizzbazz_20.txt'
my_file = open("output.txt", "a")
f = open(filename)
content = f.readlines()
f.close()
for string in content:
  list1 = string.split(" ")
  list_of_numbers=list(map(int,list1))
  counter=1
  for item in list_of_numbers:
      while counter<list_of_numbers[2]+1:
          if not counter%list_of_numbers[0] and not counter%list_of_numbers[1]:
              my_file.write("FB")
          elif not counter%list_of_numbers[0] and counter%list_of_numbers[1]:
              my_file.write("F")
          elif counter%list_of_numbers[0] and not counter%list_of_numbers[1]:
              my_file.write("B")
          else:
               my_file.write(str(counter))
          counter+=1
      my_file.write(" ")
my_file.close ()