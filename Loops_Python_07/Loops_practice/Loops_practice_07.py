# Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.



while True:
    num = int(input("Enter a number: "))
    if (num >= 1) and (num < 10): # 
        print("The given number is, ", num)
        break
    else:
        print("Provide a number between 1 to 10")
