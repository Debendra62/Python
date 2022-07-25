#praticing python

#string
stri="Be Happy"
print(type(stri))
print(stri.upper())
print(stri.strip())

name=input("enter your name ").strip()    # to ignore last spaces

print(len(name))

b=stri.split()             #string to list
print(b)
print(type(b))

c=" ".join(b)              #to join the list 
print(c)
print(type(c))

info="good morning"        #taking individual character and making uppercase
print(info[7])             #indexing negative and positive 
print(info[5].upper())
print(info[-6].upper())
print(len(info))

print(info[0:4])           #slicing
print(info[5:])

info.index("g")         #index

#string formating

name=input("Enter a string: ")
rool=input("Enter a rool number: ")
print("Your name is "+name+" and rool number is "+rool)
print("Your name is ",name)
print("your name is {} and rool no is {} .".format(name,rool))

email=input("Enter your Email: ")
name2=email[:email.index("@")]
domain=email[email.index("@") + 1:email.index(".")]
print("your name is {} and domain is {} .".format(name2,domain))
print("your domain is {1} and name is {0} .".format(name2,domain))
print(f"your name is {name2} and domain is {domain} .")
