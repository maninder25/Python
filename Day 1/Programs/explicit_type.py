# Converting string to integer to perform math
age_str = "25"
age_int = int(age_str)  # Cast to int

print(age_int + 5)     # Output: 30

# Truncation danger when converting float to int
pi = 3.99
print(int(pi))         # Output: 3 (fractional part is discarded)
