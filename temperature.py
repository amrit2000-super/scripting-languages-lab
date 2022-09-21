#Write a temperature converter python program, which is menu driven. Each such conversion  logic  should  be  defined  in  separate  functions.  The  program  should  call  the respective function based on the user’s requirement. The program should run as long as the user wishes so. Provide an option to view the conversions stored as list of tuples with attributes -from unit value, to unit value sorted by the user’s choice (from-value or to-value)

def celsius_to_farhenheit(cel):
                   far=1.8*cel+32
                   print("the temperature in farhenheit is",far)

while True:
       print("1:celsius to farhenheit")
       print("2:farhenheit to celsius")
       choice=int(input("enter the choice:\n"))
       if(choice==1):
                cel=int(input("enter the temperature in celsius:\n"))
                celsius_to_farhenheit(cel)
       elif(choice==2):
                cel=int(input("enter the temperature in celsius:\n"))
                celsius_to_farhenheit(cel)
       else:
          break   
