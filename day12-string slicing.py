#string slicing
a = "hello world"
print(len(a[0:5])) # this will print first 5 characters of the string execpt the last character
print(a[0:]) # this will print the whole string
print(a[6:]) # this will print the string from index 6 to the end of the string
print(len(a[:6]) )# this will print the string from the beginning to index 6 execpt the last character

# negative indexing in string slicing
a = "hello world"
print(a[0:-5]) # this will print the string from index 0 to index -5 (excluding the last 5 characters)
print(a[-3: -1]) # this will print the string from index -3 to index -1 (excluding the last character)
print(a[-5:]) # this will print the string from index -5 to the end