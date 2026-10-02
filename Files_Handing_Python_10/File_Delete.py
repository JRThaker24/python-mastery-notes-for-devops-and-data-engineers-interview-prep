import os

if os.path.exists("Sample_file1.txt"):
    print("Yes, File Exists")
    user_input = input("Please type 'Yes' to Delete or 'No' to not Delete: ")

    if user_input.lower() == "yes":
        os.remove("Sample_file1.txt")
        print("File deleted successfully.")
    elif user_input.lower() == "no":
        print("File is present and not deleted.")
    else:
        print("Invalid input. File not deleted.")
else:
    print("File not found")
