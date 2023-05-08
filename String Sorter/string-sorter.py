x=str(input('Please enter a string: '))
def sortstr(string):
    y=sorted(string)
    string="".join(y)
    return string
print(sortstr(x))