first_name= str(input("Please enter your first name here: "))
last_name= str(input("Please enter your last name here: "))
suffix= str(input("please enter your uni number: "))
uni= first_name[0]+last_name[0]+suffix
print ("Your Uni is:", uni )
myList=[first_name,last_name,uni]
print(myList)
myList[0],myList[1],myList[2]=myList[2],myList[0],myList[1]
print(myList)

# Was told I could do this without the middle name because I don't have a middle name #