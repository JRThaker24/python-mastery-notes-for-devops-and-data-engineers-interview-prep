# To write data in a file we have to open a file in writing mode: file = open("file.txt", "w")

file = open("Sample_file1.txt", "w")
file.write("Hello from World\n")
file.close()

file = open("Sample_file1.txt", "r")
print(file.read())
file.close()
