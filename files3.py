# Garrett Jordan

# Function to check if the word is an anagram
# Creates lists from both strings and sorts them
# Returns the result of comparison
def isAnAnagram(word, user):
    wordAsList= list(word)
    wordAsList.sort()
    inputAsList= list(user)
    inputAsList.sort()

    return (wordAsList == inputAsList)

# reads from files to list and closes file
with open('wordlist.txt', 'r') as f:
	allwords = f.readlines()
f.close()

# Creates a list of words from the files
# Strips new line
words = []
for x in allwords:
	x = x.rstrip()
	words.append(x)

# Takes input
inp = input("enter word:")
# Should really check type here...
# Creates a list from words with same length as user input
lister = [word for word in words if len(word) == len(inp) ]
# Loops through words of same length and uses function
# to check if they are anagrams.  Excludes word itself
for item in lister:
	if item != inp:
		if isAnAnagram(item, inp):
			print(item)

#Fin
