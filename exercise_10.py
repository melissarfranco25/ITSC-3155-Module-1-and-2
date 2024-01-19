userString= input("Enter a string: ")

list= list(userString)

""" my original way 
list=[]
end= len(userString)

for i in range(end):
    char1= userString[i:i+1]
    list.append(char1)
"""

print(list)

#Next line help
#https://www.freecodecamp.org/news/list-within-a-list-in-python-initialize-a-nested-list/#:~:text=Using%20list%20comprehension%20%26%20range(),using%20Python's%20range()%20function.&text=This%20creates%20a%20nested%20list%20that%20has%205%20sublists.
newList=[list[i:i+3] for i in range(0, len(list), 3)]

print(newList)               