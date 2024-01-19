list=[]

for i in range(1,11):
    num= int(input("Enter number "+ str(i) +": "))
    list.append(num)

print("Original List: ", list)

newList=[]

for elem in list:
    if(list.count(elem)==1):
        newList.append(elem)

print("Nums that apper once: ", newList)