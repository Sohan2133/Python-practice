string1=str(input("first string is:  "))
print(len(string1))
string2=str(input("second string is: "))
print(len(string2))
if len(string1)>len(string2):
    print( 'first string is larger',string1 )
elif len(string2)>len(string1):
    print('second string is larger', string2)
else:
    print('both strings are equal')