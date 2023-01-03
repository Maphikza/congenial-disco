# Implementing own .upper()

string = "I really love these small challenges."

for char in string:
    if char.islower():
        string = string.replace(char, char.swapcase())

print(string)