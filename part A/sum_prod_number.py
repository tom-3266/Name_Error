#Write a Python program to calculate sum and product of digits of a number.
#(Create Two different funtions one for sum and one product.)

listi = []
listint = []
def sum_n(n):
    n=str(n)
    for ch in n:
        listi.append(ch)
        #print(listi)
    for ch in listi:
        listint.append(int(ch))
        #print(listint)
    return sum(listint)

def prod_n(n):
    t = 1
    n=str(n)
    for ch in n:
        listi.append(ch)
        #print(listi)
    for ch in listi:
        listint.append(int(ch))
        #print(listint)
    for i in listint:
        t = t*i
    return t


x = int(input("\nEnter any number : "))
print("\nThe sum of digits of the given number is : ",sum_n(x))
listi.clear()
listint.clear()
print("\nThe product of digits of the given number is : ",prod_n(x))
listi.clear()
listint.clear()


