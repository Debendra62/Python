number=input("Number is: ")
num1=int(number)
num=num1%2
if(num==0):
    print(f"{number} is even.")
elif(num!=0):
    print(f"{number} is odd")
else:
    print("error input")
