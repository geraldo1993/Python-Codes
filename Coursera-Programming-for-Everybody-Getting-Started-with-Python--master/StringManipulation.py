#This example will demonstrate how you can do several things with strings.

#1. Convert a string to Lower Case.
#2. Convert a string to Upper Case
#3. Capitalize a String
#4. Slice substrings from a string
#5. Find a particular substring in a string
#6. Chop of leading and trailing characters from strings.
#7. Find out the length of strings
#8. Replace a substring by another.





# let us create a test string


testString1 = "Hello World!"
print "Original String: "+ testString1
# Print this string in lower case

# Converting a string to lower case

print "Converting to LowerCase"
print testString1.lower()

# Converting a string to upper case

print "Converting to Upper Case"
print testString1.upper()

# Capitalizing a string

# Only the first letter in the string will be capitalized
print "Capitalizing the String"
print testString1.capitalize()

# Trying to slice out a substring between given indexes

print "Substring from index 1 to 7"
print testString1[1:8]

#Substring from the start till character at index = 7 (start of string is index 0)
print "Substring from the start till character at index = 7 (start of string is index 0): "
print testString1[:8]

#Substring from the character at index = 7, till the end of the string (remember: start of string is index 0)
print "Substring from the character at index = 7, till the end of the string (remember: start of string is index 0): "
print testString1[7:]


#Find the position of a  substring within the string

#This gives us the first index during a left to right scan. If the string is not found, it returns -1
print "Find the index from which the substring 'llo' begins within the test string"
print testString1.find('llo')

print "Now, let's look for a substring which is not a part of the given string"
print testString1.find('xxy')

# Now, trying to find the index of a substring between specified indexes only
print "Now, trying to find a substring between specified indexes only: looking for 'l' between 4 and 9"
print testString1.find('l',4,9)

# rfind is used, to find the index from the reverse
# So, testString1.rfind('l') will look for the last index of l in the string
print "find('l') on the given string returns the following index (scanning the string from left to right):"
print testString1.find('l')

print "rfind('l') on the given string returns the following index (this scans the string from right to left):"
print testString1.rfind('l')

# Now let us try to replace/substitute a substring of this string with another string

print "Replacing World with Planet"
print testString1.replace("World","Planet")


# Now let us try to split the string, into separate words

# let us split it wherever there is a space
print "Splitting the string into words, wherever there is a space"
print testString1.split(" ")
print testString1.rsplit(" ")

# Remove leading and trailing whitespace characters

testString2 = "Hello World!  "
print "Current Test String=" + testString2
print "Length (there are whitespaces at the end):" + `len(testString2)`
print "Length after stripping "+ `len(testString2.strip())`
