# Reverse String
text = input("Enter a string: ")

reverse_text = ""
for char in reversed(text):
    reverse_text += char
print(reverse_text)