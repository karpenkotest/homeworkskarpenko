def func_lower(string_of_text):
    lower=string_of_text.lower()
    return lower

def func_upper(string_of_text):  
    upper=string_of_text.upper()
    return upper

string_of_text=input("Enter a string: ")
print(func_lower(string_of_text))
print(func_upper(string_of_text))
