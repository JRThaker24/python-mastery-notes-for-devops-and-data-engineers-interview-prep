file1 = open("Sample_file.txt", "r")
file2 = open("Sample_file1.txt", "w")

for line in file1:
    file2.write(line)

file1.close()
file2.close()

file2 = open("Sample_file.txt", "r")
print(file2.read())
file2.close()