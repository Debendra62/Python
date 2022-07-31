pamount=float(input("Enter the purchased amount: "))
print(type(pamount))
if pamount>=5000:
    discount=0.1*pamount
    print(f"{discount} is the discount amount of {pamount}.")
elif pamount>=4000 or pamount<5000:
    discount=0.07*pamount
    print(f"{discount} is the discount amount of {pamount}.")
elif pamount>=3000 or pamount<4000:
    discount=0.05*pamount
    print(f"{discount} is the discount amount of {pamount}.")
elif pamount>=2000 or pamount<3000:
    discount=0.03*pamount
    print(f"{discount} is the discount amount of {pamount}.")
else:
    discount=0.02*pamount
    print(f"{discount} is the discount amount of {pamount}.")
    
    
    
