#string formating


email=input("Enter your Email: ")
name2=email[:email.index("@")]
domain=email[email.index("@") + 1:email.index(".")]
print("your name is {} and domain is {} .".format(name2,domain))
print("your domain is {1} and name is {0} .".format(name2,domain))
print(f"your name is {name2} and domain is {domain} .")

import mymodule
mymodule.greeting("dev")
