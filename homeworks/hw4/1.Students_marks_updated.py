marks={"Ivanov": [1], "Petrov": [10, 5, 8, 2],"Kozlov": [11, 5, 8], "Karpenko": [12,12]}
print(marks)
for val in marks:
    average_mark=sum(marks[val])/len(marks[val])
    #print(average_mark)
    marks.update({val: average_mark})
    #print(marks)
for key in marks:
    maximum=max(marks.values())
    minimum=min(marks.values()) 
#print(maximum, minimum)
for key in marks:
  if marks[key]==maximum:
       print(f'Max average mark {maximum} has: {key}')
  if marks[key]==minimum:
       print(f'Min average mark has {minimum} has: {key}')
