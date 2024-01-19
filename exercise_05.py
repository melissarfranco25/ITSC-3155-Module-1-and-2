firstList=[]
secondList=[]

commonList=[]

for i in range(5):
    num=int(input("Enter a number for the first list: "))
    firstList.append(num)

for j in range(5):
    num=int(input("Enter a number for the second list: "))
    secondList.append(num)

print("First List: ", firstList)
print("Second Llist: ", secondList)

for elem in firstList:
    for elem2 in secondList:
        if elem == elem2:
            commonList.append(elem)

commonList= list(set(commonList))
        
print("Common List: ", commonList)