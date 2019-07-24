import string
str=input("enter String")
letters=0
for i in str:
    if i in string.ascii_letters:
        letters+=1
print(letters)