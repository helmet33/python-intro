# Garrett Jordan

words = []

# Function to check if the word is an anagram
# Creates lists from both strings and sorts them
# Returns the result of comparison
def isAnAnagram(word, user):
	wordList= list(word)
	wordList.sort()
	#inputList= list(user)
	#inputList.sort()
	return (wordList == user)

def getAnagrams(user):
	lister = [word for word in words if len(word) == len(user) ]
	for item in lister:
		if isAnAnagram(item, user):
			yield item

# reads from files to list and closes file
with open('wordlist.txt', 'r') as f:
	allwords = f.readlines()
f.close()

# Creates a list of words from the files
# Strips new
for x in allwords:
	x = x.rstrip()
	words.append(x)
inp = 1

# Takes input
while inp != "99":
	inp = input("enter word:")
	wet = list(inp)
	wet.sort()
	result = getAnagrams(wet)
	print(list(result))

# Should really check type here... but type is always a string
# Creates a list from words with same length as user input
##	lister = [word for word in words if len(word) == len(inp) ]
# Loops through words of same length and uses function
# to check if they are anagrams.  Includes the word itself
#	for item in lister:
#		if isAnAnagram(item, inp):
#			print(item)

#Fin
