Write a program that prints the next 20 leap year and sum of digits of leap year must be greater than 16

Program :

def leap_yr_20(n):
    list1 =[]
    listi =[]
    listint = []
    count =0
    while count < 20:
        if (n%4 == 0 or n%400==0 and n%100 ==0):
            k=str(n)
            for ch in k:
                listi.append(ch)
            #print(listi)
            for ch in listi:
                listint.append(int(ch))
            #print(listint)
            sum_int = sum(listint)
            #print(sum_int)
            if sum_int > 16 :
                list1.append(n)
                count+=1
            listi.clear()
            listint.clear()
        n+=1
​
    return list1
​
n = int(input("Enter the year : "))
list1 = leap_yr_20(n)
print("These are the 20 leap years after given year {} with sum greater than 16 : ".format(n),list1)
