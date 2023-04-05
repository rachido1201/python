
def convert(amount):

    total= amount * 50

    message  = " the  amount * price  " 

    message1 = " is the total  ."

    result = message + str(total) + message1
    
    return result

userinput = input("which is the amount ? " :)

if userinput == 100000:
 print("that is a lot!")

if  float(userinput) > 100000:
   print("that is too much !")