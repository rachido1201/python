
import csv
text_file = open("myfile.txt")

content = text_file.readline()
print(content)

content = text_file.readline()
print(content)

text_file.close()