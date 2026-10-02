

str = "Python"
print(" --- To find length of a string--- ")
print(len(str))

print("\n")
print(" --- Replace a string--- ")
new_str= str.replace("t","T")
print(new_str)

print("\n")
print(" --- Remove white space from the begining or the end--- ")
str2 = " Python "
print(str2.strip())

print("\n")
print(" --- Change String to Upper case--- ")
str3= "python"
print(str3.upper())

print("\n")
print(" --- Change String to Lower case--- ")
str4 = "PYTHON"
print(str4.lower())

print("\n")
print(" --- Split the string in python--- ")
str5= "Python,Language"
str6= "Python-Scripting-Language"
print(str5.split(","))
print(str6.split("-"))
print(str6.count("P"))
