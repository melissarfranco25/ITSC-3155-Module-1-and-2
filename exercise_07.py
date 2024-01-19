num= input("Enter a number or QUIT to quit: ")
list=[]

while num != 'QUIT':
    list.append(int(num))
    num= input("Enter a number or QUIT to quit: ")

print("All Nums: ", list)

evenList=[]

for elem in list: 
    if elem%2==0:
        evenList.append(elem)
print("Even Nums: ", evenList)