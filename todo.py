MyToDoList = ["buy christmas gifts","buy clothes","buy food","buy christmas toys","buy a new phone","buy shoes","buy a house","buy jewlery","buy a car", "clean the house","clean my room", "clean my phone"]
#print(MyToDoList)
#print (len(MyToDoList))
#print(MyToDoList.index("buy clothes"))
#print (MyToDoList)

if len(MyToDoList) > 0:
  print ("what would you like to add?")
add = input()
MyToDoList.append(add)
print(MyToDoList)
