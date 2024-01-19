str1 = input("Enter a string: ")
str2 = input("Enter another string: ")

if(len(str1) < len(str2)):
    print(str2.endswith(str1))
else:
    print(str1.endswith(str2))
    