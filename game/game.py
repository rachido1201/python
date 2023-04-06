# setup

import random
answer = random.randint(1,101)
guess_number = 0
user_wins = False
attempts = 0


#loop

while user_wins is True :

#user input


        guess = input ("Enter a number between 1 and 101 :")  

try :

    guess_number = int(guess)

    #check input

except :

    print (" you have a invalid number !!")


#increase attempt

attempts += 1

#check the secret number

if guess_number == answer:
    user_wins = True

elif guess_number > answer:

 print ("the secret number is bigger")


elif guess_number < answer:
    
    print ("the secret number is bigger")

#loop
if  attempts == 1 :
 
 attempt_word = "attempt"

else:

 attempt_word = "attempts"

#display
print (" you have found the number !")

