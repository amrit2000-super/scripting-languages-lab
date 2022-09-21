def AtomicDictionary():
#Creating a dictionary that contains the atomic element symbol and its name
            name={'S':'Sulphur','C':'Carbon','O':'Oxygen','H':'Hydrogen'}
            print(name)

#Adding a unique element into this dictionary by interacting with the user
            addelement=input("enter the element u want to insert:\n")
            nameelement=input("enter the name of the element you want to insert:\n")
            name[addelement]=nameelement
            print(name)

#Adding a duplicate element into this dictionary by interacting with the user
            addelement=input("enter the element u want to insert:\n")
            nameelement=input("enter the name of the element you want to insert:\n")
            name[addelement]=nameelement
            print(name)

#Display the number of atomic elements in this dictionary
            print("the no of elements in the dictionary are",len(name))

#Ask user to enter an element to search in the dictionary. Display appropriate results
            elesearch=input("enter the element you want to find:\n")
            if(name.get(elesearch)):
                    print("element is present\n")
            else:
              print("element is not present\n")