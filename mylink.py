my_list=[];# creating an empty list,my_list
my_list.append(10);my_list.append(20);my_list.append(30);my_list.append(40);# append 10,20,30,40
my_list[1]=15 #Insert the value 15 at the second position in the list.
my_list.extend([50,60,70]) #Extend my_list with another list: [50, 60, 70].
my_list.pop() #Remove the last element from my_list.
my_list.sort() #sorting my_list
if 30 in my_list: #to find 30
    print(my_list.index(30))#to get and print the index of 30