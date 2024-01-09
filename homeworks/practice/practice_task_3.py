filename = 'numbers.txt'
f = open(filename)
content = f.readlines()
for string in content:
  list1 = string.split(";")
  print(list1)
  n = list1[0]
  k = list1[1]
  n = n.split()
  k = k.split()
  N = list(map(int, n))
  sum = 0
  lenth = len(N)
  for item in N:
    sum = sum + item
    whole_part = sum // lenth
    rest_part = sum % lenth
  print(whole_part)
  print(rest_part)
  if whole_part == int(k[0]) and rest_part == int(k[1]):
    print("Happy to inform you that you and your calculations are amazing!")
  else:
    print("Looks like you should have more practice in mathematics!")
