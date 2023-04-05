
business_card = {"Name": "Vero",
                    "Last name": "Nes",
                    "City": "tokyo",
                    "Phone number": 12012012012,
                    "email": "xxx@gmail.com"}

print(business_card["Phone number"])
print(business_card["City"])

import random

for i in range(5):
    print( random.randint(1, 51))

    answer_is_correct = True

if answer_is_correct:
    print("The answer is correct!")


number = input("Type a number: ")

try:
    result = int(number) + 1
    print("The result is " + str(result))

except:
    print("Couldn't convert your input to a valid number")
    quit()