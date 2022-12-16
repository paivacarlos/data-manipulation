import csv

#writing a new csv_file
with open("utils_file/numbers.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(("first", "second", "third"))
    writer.writerow((28, 89, 33))
    writer.writerow((10, 20, 30))

#reading a csv_file
with open("utils_file/numbers.csv", "r") as file:
    reader = csv.reader(file)
    for x in reader:
        print("Number of collum: ", len(x))
        print(x)

#creating a list with file_csv
data_list_from_csv_file = []

with open("utils_file/numbers.csv", "r") as file:
    reader = csv.reader(file)
    data_list_from_csv_file = list(reader)

print(data_list_from_csv_file)

#reading a list since second line
for line in data_list_from_csv_file[1:]:
    print("here: ", line)