anything = float(input("Enter a number:"))
something = anything ** 2
print(anything ,"to the power of 2 is", something)

#to find the hypotenuse of a triangle
leg_a = float(input("Enter the first length:"))
leg_b = float(input("Enter the second legnth:"))
hypotenuse = (leg_a ** 2 + leg_b ** 2) ** 0.5
print("The hypotenuse legnth is", hypotenuse)


#STRING OPERATORS THE "+" CONCATENATOR
fname = input("Enter your first name:")
lname = input("Enter your last name:")
print("Welcome home " + fname + " " + lname + "")

#THE REPLICATOR"*" STRING OPERAtor
print("James" * 5)

#THE STRING() FUNCTION
leg_a = float(input("Enter value of first leg"))
leg_b = float(input("Enter the value of second leg"))
print("The hypotenuse length is" + str((leg_a**2 + leg_b**2)**.5))# we can pass the print as a string 
