list=[]

for i in range(5):
    userString= input("Enter a word: ")
    list.append(userString)

print("Words: ", list)

# oneString = ''
# for elem in list:
#     oneString+= (elem + " ")

# print("One String: " , oneString)
# OOOOOOORRRRRR

oneString = ' '.join(list)
print("One String:", oneString)