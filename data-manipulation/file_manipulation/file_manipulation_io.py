#opening file to read
file1 = open("utils_file/file_01.txt", "r")

#reading file
print(file1.read())

#couting characteres number
print(file1.tell())

#return to init file
print(file1.seek(0,0))

#read the first ten chars
print(file1.read(10))

#recording file
file2 = open("utils_file/file_02.txt","w")
file2.write("Testing recording file")
file2.close()

file3 = open("utils_file/file_02.txt")
print(file3.read())

#append text in te file
file4 = open("utils_file/file_02.txt", "a")
file4.write(" more text")
file4.close()
file5 = open("utils_file/file_02.txt", "r")
print(file5.read())