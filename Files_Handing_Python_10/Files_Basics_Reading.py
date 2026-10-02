# Handling file is a very important task, we can read content, write content, copy and many more
# Files are stored in 'ROM'
# To open a file we use: open("file_name.txt", "mode")
# here mode are in:
# 'r': read, 'w': write, 'a': append, 'r+', 'w+', 'a+'
# To read a file we use .read(): file = open("file.txt", "r") and file.read() and prit(file.read())
# To specify specifc text characters  and line we use: file.read(10) and file.readline()

file = open("Sample_file.txt", 'r')
print(file.read())
#print(file.read(10))
#print(file.readline())
#print(file.readline())
# print(file.readlines(300))
file.seek(0) # rewind to start
print("---Printing file using for loop---")
for x in file:
    print(x)
print("---At the end we close the file---")
file.close()    