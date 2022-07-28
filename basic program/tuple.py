#tuple(ordered,not changeable,allow duplicates)

tup=()
print(type(tup))

tup2=(1,2,3,4)
li=list(tup2)                      #Convert tuple to list to change the data
print(type(li))


tup2=tup2+(5,6,7)+tup2             #adding data
print(tup2)

tup3=(1,2,3,4,5,6,7,8)
p,q,*r=tup3                        #unpacking tuple
print(p)
print(q)
print(r)
