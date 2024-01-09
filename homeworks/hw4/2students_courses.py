Python={'Karpenko', 'Ternenko','Afanasenko','Denisenko'}
Java={'Karpenko', 'Lapushenko'}
Fullstack={'Vasilenko','Ternenko'}
Frontend={ 'Prokopenko', 'Lapushenko','Kozlenko'}
visit_several_courses=Python&Java|Fullstack&Frontend|Python&Frontend|Fullstack&Java|Python&Fullstack|Java&Frontend
print(f'These students visit several courses:{visit_several_courses}')
not_frontend_students=(Python|Java)-Fullstack-Frontend
print(f'These students do not study Frontend and Fullstack:{not_frontend_students}')  
python_or_java=Java^Python
print(f'These students study Pythond or Java:{python_or_java}. Please note, studens that study both Python and Java are not included.')
python_or_and_java=Java|Python
print(f'These students study Pythond or Java:{python_or_and_java}. Please note, studens that study both Python and Java are  included.')







