vowels = ['a','e','i','o','u']
word = "Milliways"
found = []
# simple adjustment to vowels.py that appends all found vowels and prints
# found as list.
for letter in word:
    if letter in vowels:
        found.append(letter)
print(found)

# the following is actual vowels2.py as per instructions in the book.
# we're going to look at all letters in word, then check if letters in vowels
# THEN check if we've already found those vowels, if not, append to found list
found = []
# found = [] is needed to clear the list before this next suite runs
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)
    
        
