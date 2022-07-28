a=[]
a.extend(["apple","pineapple","grapes"])
print(a)

a.insert(1,"banana")
print(a)

a.append("mango")
print(a)

a.sort(reverse=True)
print(a)

b=a.pop(-2)
c=b.upper()
print(c)

print(f"{b} is the fetch item")

