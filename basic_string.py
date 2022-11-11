string = input("Enter any string : ")
print("The total number of characters in the string are",len(string))
for i in range(10):
    print(string)
print("The first character of the string is :",string[0])
print("The first three characters of the string are",string[0:3])
print("The last three characters of the string are",string[-3:])
print("The string backwards is",string[::-1])
if len(string)>=7:
    print("The seventh character of the string is",string[6])
else:
    print("The string is not long enough for having seventh character")
print("The string with first and last character removed is",string[1:-1])
print("The string in all caps is",string.upper())
print("The string with every 'a' replaced with 'e' is",string.replace('a','e'))

