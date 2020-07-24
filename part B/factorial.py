#Develop a Python Program which prints factorial of a given number (Number should be User defined)

x = int(input("Enter the number : "))
if x < 0:
    print("\nFactorial of negative numbers does not excist")
elif x == 0:
    print("\nFactorial of 0 is 1")
else:
    y = x
    z=1
    while y > 0:
        z = z * y
        y = y - 1
print("\nThe factorial of {} is ".format(x),z)
