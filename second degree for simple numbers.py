def square(x):
    y=x+1
    return simple(y)

#print (square(5))

def simple(n):
    return n**2



my_list=list(map(square,range(2,51)))
print(my_list)