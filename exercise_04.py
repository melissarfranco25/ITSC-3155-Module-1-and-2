num = int(input("Enter a number: "))

list=[]

for i in range(num):
    newFloat= float(input("Enter number "+ str(i+1) +": "))
    list.append(newFloat)


print("List:", list)

sum=0
for elem in list:
    sum= sum+elem

average= sum/num

print("Average: " + str(average))