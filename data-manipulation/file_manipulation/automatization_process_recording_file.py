#send a file name
fileName = input("Digit files name: ")
fileName = fileName + ".txt"

#recording the with the name
file1 = open(f"utils_file/{fileName}", "w")

#recording a data in this file
file1.write("Writing some text")
file1.close()

#reading the file
file2 = open(f"utils_file/{fileName}", "r")
print(file2.read())
file2.close()