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