f1 = open("main.py")
content1 = f1.read() # as a string
f1.close()
reversed=content1[::-1]
print(reversed)