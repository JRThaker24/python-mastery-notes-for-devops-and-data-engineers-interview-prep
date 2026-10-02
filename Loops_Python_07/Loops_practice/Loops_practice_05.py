# Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

name = "chichir na ruchir"
for char in name:
    if name.count(char) == 1:
        print(f"Non-Repeated Character {char}")
        break
