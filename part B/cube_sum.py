#Develop a Python Program which prints  cube sum of first n natural numbers (N is user defined)

x = int(input("Enter the boundary : "))
sum_cube =0
for i in range(x):
    c = i**3
    #print(c)
    sum_cube = sum_cube + c
print("\nSum of cube of first {} natural numbers is : ".format(x),sum_cube)