#Design a user interactive Calculator .( sum , subtraction , multiplication , division , Distance , speed , Intrest)

#defining functions for calculator
def sumi(a,b): #addition
    return a+b
def subs(a,b): #difference
    return a-b
def mult(a,b): #multiplication
    return a*b
def div(a,b):  #division
    return a/b
def interest():  #simple interest
    P = float(input("\nEnter the principle amount : "))
    R = float(input("Enter the rate of interest per year : "))
    t = float(input("Enter the duration : "))
    print("1. months")
    print("2. years")
    q = str(input("Enter duration type(months/years) :"))
    if q=="months":  #for month to year convertion
        time = t/12
    elif q=="years":
        time = t
    else:
        print("**** Wrong choise *****") #choise validation
    r = R/100
    si = P*(1 + (r*time))
    return (si,q,P,t)
def value_cal():  # funtion to input values
    num1 = int(input("\nEnter the first number : "))
    num2 = int(input("Enter the second number : "))
    return(num1,num2)
def contin():
    cont = input("\nDo you want to continue (Y/N) : ")
    return cont

def main_calc():
    while cont == "Y" or cont == "y":      # main choise for interactive calculator
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Calculate Distance")
        print("6. Calculate Speed")
        print("7. Calculate Interest")
        print("8. Exit")
        try:
            ch = int(input("\nEnter the choice from the following : "))
            return ch
        except:
            print("wrong input")
            break
    else:
        for i in range(1):
            break
        
cont = "Y"
print("\n\t\tSimple Calculator")
while True:
    ch = main_calc()
    if ch==1:  # nested if for selecting based on choise
        a,b = value_cal()
        c = sumi(a,b)
        print("\nThe sum of {} and {} is :".format(a,b),c)
        cont = contin()

    elif ch==2:
        a,b = value_cal()
        c = subs(a,b)
        print("\nThe difference of {} and {} is :".format(a,b),c)
        cont = contin()

    elif ch==3:
        a,b = value_cal()
        c = mult(a,b)
        print("\nThe product of {} and {} is :".format(a,b),c)
        cont = contin()

    elif ch==4:
        a = int(input("\nEnter the dividend : "))
        b = int(input("Enter the divisor : "))
        c = div(a,b)
        print("\nThe quotient of {} and {} is :".format(a,b),c)
        cont = contin()

    elif ch==5:
        a = int(input("\nEnter the speed (km\h) : "))
        b = int(input("Enter the time (hr) : "))
        c = mult(a,b)
        print("\nThe distance covered : {}kms".format(c))
        cont = contin()

    elif ch==6:
        a = int(input("\nEnter the distance covered (km) : "))
        b = int(input("Enter the time (hr) : "))
        c = div(a,b)
        print("\nSpeed : {}km/hr".format(c))
        cont = contin()

    elif ch==7:
        sim_int,q,P,t = interest()
        print("\nThe simlpe interest for ₹{} for {}{} is : ".format(P,t,q),sim_int)
        cont = contin()

    elif ch==8 or cont =="N" or cont == "n":  # for breaking from loop
        print("\n\t\t*** Thank you ***")
        break

    else : 
        print("\n\t\t*** Wrong Choise ***")
        break


