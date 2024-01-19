def cubes(num):
    return num**3

num = int(input("Enter an integer greater than 1: "))

for i in range(num+1):
    print("The cube of ",i," is ", cubes(i) )