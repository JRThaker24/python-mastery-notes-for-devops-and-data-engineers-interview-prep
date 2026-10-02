print("\n")
print("--- Detailed Explanation of '*' programme with Outer-Inner Loops ---\n")

i = 1
all_rows = ""
while i <= 5:
    print(f"➡️ Outer loop starts: i = {i}")
    print("   This means we are starting a NEW ROW of stars")

    j = 1
    row_output = ""   # collect stars for one row
    while j <= 5:
        print(f"      Inner loop iteration: j = {j}")
        print("      → Printing one star (*) without moving to the next line")
        row_output += "*"   # add star to row
        print("We have reach Till: ",row_output)
        j += 1
        print(f"      Now j becomes {j}\n")

    # After finishing inner loop (5 stars)
    print(f"   ✅ Inner loop finished for i = {i}, full row created: {row_output}")
    print(row_output)   # actually print the row of stars
    print("   (Cursor moved to next line for the next row)\n")
    all_rows += row_output + "\n"
    print(f"We have reach Till: , \n {all_rows}, when 'i' is {i}")
    i += 1
    print(f"➡️ Now i becomes {i}, outer loop will check condition again\n")
    

print("✅ Programme finished. We have created a 5x5 block of stars!")
