'''Create a list of all odd numbers between 1 and a max number.
Max number is something you need to take from a user using input() function'''
oddnumber=[]
num=1
number=int(input("Enter a number: "))
for i in range(1,number):
    if i%2==1:
        oddnumber.append(i)
print("Here's the odd number list",oddnumber) 
    
