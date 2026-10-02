# To print vaules of variables including 'strings' and integers together we can do with many ways

name = "Python"
year = "2025"


print(" Using comma (',') ")
print("Name: ", name, "Year: ", year)

print("\n")
print(" Concatenate using ('+') ")
print("Name: "+  name + " Year: "+ str(year) )

print("\n")
print(" using 'str.format()' ")
print("Name: {} Year: {}".format(name,year))

print("\n")
print(" using 'str.format()' using positions ")
print("Name: {0} Year: {1}".format(name,year))

print("\n")
print(" using 'str.format()' using key-vaule")
print("Name: {n} Year: {y}".format(n=name,y=year))

print("\n")
print("Simplest and most effective way is to add 'f' at starting")
print(f"Name: {name} Year: {year}")

