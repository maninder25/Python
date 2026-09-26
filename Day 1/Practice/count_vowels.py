# Count Vowels
text = input("Enter a string: ").lower()
print(sum(1 for char in text if char in "aeiou"))