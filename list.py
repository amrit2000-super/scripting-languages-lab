#creating list with inputs from user
lst=[]
n = int(input("enter the no of elements of the list:\n"))
counter=0
for x in range(n):
               ele=input("enter the element to be inserted into the list\n")
               lst.append(ele)
print("the elements of the list are\t",lst)

#determine min and max elements in the list
print("minimum element in the list is",min(lst))
print("maximum element in the list is",max(lst))

#insert new element into the list
nele=input("enter new element:\n");
lst.append(nele)
print("the elements of the list are\t",lst)

#Delete an element from the list
ndel=input("enter element to be deleted:\n")
lst.remove(ndel)
print("the elements of the list are\t",lst)

#Determine if an element is present in the list
elep=input("enter element to be found:\n")
for i in lst:
            if(i==elep):
                 counter=1
if(counter==1):
             print("element is present in the list")
else:
    print("element is not present in the list")
           

