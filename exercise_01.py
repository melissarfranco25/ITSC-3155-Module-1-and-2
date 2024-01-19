grade = int(input('Enter a grade from 0 to 100:'))

if grade > 89:
    print("Your grade is an A")

elif grade > 79:
    print("Your grade is a B")

elif grade > 69:
    print("Your grade is a C")
    
elif grade > 59:
    print("Your grade is a D")

else:
    print("You have an F")