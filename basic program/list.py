#List (ordered,Changeable,Allow duplicates)

a=[1,"apple",1.3,True]          #heterogenious list
b=list((1,2,"HI"))
print(type(a))
print(type(b))

game=["football","Basketball","Chess","cricket"]  #list(ordered)
print(game)

game[1]="badminton"                               #list(changeable)
print(game)


game[2]="Football"                                  #list(allow dublicates)
print(game)

game.sort()                                         #sort(smaller to larger)
print(game)

game.sort(reverse=True)                             #sort(larger to smaller)
print(game)

"""   insert() ---->  remove()
      append() ---->  pop()
      extend() ---->  -----
               ---->  del()          #clear the list totally
               ---->  clear()        #clear the list but empty list exist
"""

game.insert(1,"Ludo")                              #insert(add element to list) imp
print(game)

game.append(["hockey","Horse racing"])            #append(add element to last of list)
print(game)
print(game[-1])

game.extend(["pubg","clash royale"])              #extend(add list to another list as individual)
print(game)








