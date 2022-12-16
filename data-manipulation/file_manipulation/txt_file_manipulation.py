import os

text = "Data scientist is very important,"
text = text + " because we need someone that can read our data,"
text = text + " therefore there is so necessary."

file_created = open(os.path.join("utils_file/scientist.txt"), "w")

#recording the data in the file
for data in text.split():
    file_created.write(data+" ")

file_created.close()

file_to_read = open("utils_file/scientist.txt", "r")
data_of_file = file_to_read.read()
file_to_read.close()

print(data_of_file)

#Using the expression WITH
data_using_expression_with = None
with open("utils_file/scientist.txt", "r") as file:
    data_using_expression_with = file.read()

print(len(data_using_expression_with))
print(data_using_expression_with)
