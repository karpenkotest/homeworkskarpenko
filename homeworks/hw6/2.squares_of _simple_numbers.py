def square(num):
  return num ** 2

def simple(n):
  d= 2
  while n % d != 0:
      d += 1
  return d == n

squared_simple_numbers = list(filter(simple, range(2,51)))

for item in squared_simple_numbers:
    print(f"{square(item)}")
