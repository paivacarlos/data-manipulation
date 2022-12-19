#writing a csv by row
file1 = open("utils_file/salaries.csv", "r")
data = file1.read()
rows = data.split('\n')
print(rows)
file1.close()

#wrinting a csv by collum
file2 = open("utils_file/salaries.csv", "r")
data2 = file2.read()
rows = data2.split('\n')
full_data = []

for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)

print(full_data)

#number od rows
count = 0
for row in full_data:
    count += 1
print(f"Number of lines: {count}")
