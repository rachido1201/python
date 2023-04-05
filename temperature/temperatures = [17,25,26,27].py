temperatures = ["freeze","cold","hot","very hot"]

temperatures.sort()

print(temperatures [0])
print(temperatures [1])
print(temperatures [2])
print(temperatures [3])

temperatures.append("the temp is  very  hot")

temperatures_count= len(temperatures)

print("the temp is " + str(temperatures_count) + " degrees which is cold ")

temperatures.pop(2)

print (temperatures)

print (len(temperatures))
