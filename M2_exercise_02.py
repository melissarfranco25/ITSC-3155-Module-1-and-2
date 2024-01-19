stringInput = input("Enter a string: ")

lowString= []
upString =[]

for elem in stringInput:
    if elem.islower():
        lowString.append(elem)
    elif elem.isupper():
        upString.append(elem)

lowString.extend(upString)
oneString= ''.join(lowString)

print(oneString)