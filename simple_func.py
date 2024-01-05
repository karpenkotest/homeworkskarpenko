def simple(n):
    for j in range(2, n):
        if not n % j and n!=j:
           break
        else:
            return(n)

print(list(map(simple,range(2,50))))

