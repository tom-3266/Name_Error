#Develop a python program which print sum of all the Integers in a list 
#( Note  : All the elements must be user defined and list must contain strings also ) 


tmp_lis = []
while True:
    x = input("\nEnter the value to be entered to list : ")
    tmp_lis.append(x)
    y = input("Do you want to enter more elements to list(Y/N) : ")
    if y == "Y" or y =="y":
        continue
    elif y == "n" or y == "N":
        break
    else :
        print("*** Wrong Input ***")
        break
print("\nThe final list is : ",tmp_lis)     

new_lis =[]
for i in tmp_lis:
    if i.isdigit() == True:
        new_lis.append(int(i))
print("\nThe sum of integers in list : ",sum(new_lis))
