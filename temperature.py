#Write a temperature converter python program, which is menu driven. Each such conversion  logic  should  be  defined  in  separate  functions.  The  program  should  call  the respective function based on the user’s requirement. The program should run as long as the user wishes so. Provide an option to view the conversions stored as list of tuples with attributes -from unit value, to unit value sorted by the user’s choice (from-value or to-value)

tpl={}

def celsius_to_farhenheit(cel):
    far = 1.8 * cel + 32
    print("the temperature in farhenheit is", far)
    tpl[cel]=far

def farhenheit_to_celsius(far):
    cel = 5/9*(far-32)
    print("the temperature in farhenheit is", far)
    tpl[far]=cel

def celsius_to_kelvin(cel):
    kel=cel+273
    print("the temperature in kelvin is",kel)
    tpl[cel]=kel

def kelvin_to_celsius(kel):
    cel = kel-273
    print("the temperature in farhenheit is", cel)
    tpl[kel]=cel

def farhenheit_to_kelvin(far):
    kel = 5/9*(far-32)+273
    print("the temperature in kelvin is", kel)
    tpl[far]=kel

def kelvin_to_farhenheit(kel):
    far = 9/5*(kel-273)+32
    print("the temperature in farhenheit is", far)
    tpl[kel]=far

while True:
    print("1:celsius to farhenheit")
    print("2:farhenheit to celsius")
    print("3:celsius to kelvin")
    print("4:kelvin to celsius")
    print("5:farhenheit to kelvin")
    print("5:kelvin to farhenheit")
    choice = int(input("enter the choice:\n"))
    if (choice == 1):
        cel = int(input("enter the temperature in celsius:\n"))
        celsius_to_farhenheit(cel)
        print(tpl)
    elif (choice == 2):
        far = int(input("enter the temperature in farhenheit:\n"))
        farhenheit_to_celsius(far)
        print(tpl)
    elif (choice==3):
        cel = int(input("enter the temperature in celsius:\n"))
        celsius_to_kelvin(cel)
        print(tpl)
    elif (choice==4):
        kel = int(input("enter the temperature in kelvin:\n"))
        kelvin_to_celsius(kel)
        print(tpl)
    elif (choice==5):
        kel = int(input("enter the temperature in farhenheit:\n"))
        farhenheit_to_kelvin(far)
        print(tpl)
    elif (choice==6):
        kel = int(input("enter the temperature in farhenheit:\n"))
        kelvin_to_farhenheit(kel)
        print(tpl)
    else:
        break
