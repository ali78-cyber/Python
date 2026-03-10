a = "@@@@@ali raza!!!"
print (len(a)) # string length
print (a.find("a", a.find("a") + 1))

# strings are always in immutable

print (a.upper()) # convert to upper case
print (a.lower()) # convert to lower case
print (a.rstrip("!")) # remove the ! from the right side of the string it did not remove from the left side of the string
print (a.lstrip("@")) # remove the @ from the left side of the string it did not remove from the right side of the string
print (a.replace("ali","aliraza")) # replace ali with aliraza
print(a.split(" "))
blog = "this is my first blog"
print(blog.capitalize()) # capitalize the first letter of the string
blog1 = "this is my first blog"
print(blog1.title()) # capitalize the first letter of each word in the string
str1 = "hello world"
print(len(str1)) # length of the string
print(str1.center(20,"x")) # center the string with x on both sides
print(str1.count("l")) # this will count the number of times l appears in the string
print(str1.endswith("d")) # this will check if the string ends with d
print(str1.startswith ("h")) # this will check if the string with h return the boolean value true or false
str2 = "Hi guys my name is aliraza and i am a python developer and also  i build nn workflows"
print (str2.find("i")) # this will return the index of the first occurance of i in  the string
print (str2 .find("i", str2.find("i") + 1)) # this will return the index of the second occurance of i in the string
print (str2.isalnum()) # this will check if the string is a alphanumeric or not return boolean value true of false
str3 = "alikhan"
print (str3.isalpha()) # this will check if the string is a alphabet or not return boolean value true of false
str4 = "helllo universe"
print (str4.islower()) # this will check if the string is in lower case or not return boolean value true of false
str5 = "HELLO UNIvERSE"
print (str5.isupper()) # this will check if the string is in upper case or
str6 = "     "
print (str6.isspace()) # this will check if the string is a space or not return boolean value true of false
print (str5.swapcase()) # this will swap the case of the string