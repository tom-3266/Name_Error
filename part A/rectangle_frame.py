#Write a function that takes a list of strings an prints them, one per line, in a rectangular frame.
#For example the list ["Hello", "World", "in", "a", "frame"] gets printed as:
'''
*******
*Hello*
*world*
*in   *
*a    *
*frame*
*******
'''

sentence = input("\nEnter the list of strings : ")
sen_list = []
new_lis = []
y=0
x = sentence.split()
t = len(x)
for i in x:
    if len(i) > y:
        y=len(i)
#print(y)
#print("*" * (y+2))
new_lis.append("*" * (y+2))
for i in range(t):
    new_lis.append("*"+ x[i]+ (" " * ((y) - len(x[i]))) +"*")
new_lis.append("*" * (y+2))
#print(new_lis)
print("\n\n")
for i in range(len(new_lis)):
    print(new_lis[i])
    