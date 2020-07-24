#Develop a Python program to print all Prime numbers in a given Interval (Interval values should be user defined)

lower = int(input("Enter lower limit : "))# getting the upper and lower limit
upper = int(input("Enter upper limit : "))
prime_lis = [] #for generating prime number list

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           prime_lis.append(num)
            
print("Prime numbers between", lower, "and", upper, "are : ",prime_lis)