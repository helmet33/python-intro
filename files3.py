# Garrett Jordan

words = []

# Function to check if the word is an anagram
# Creates lists from both strings and sorts them
def isAnAnagram(word, user):
	wordList= list(word)
	wordList.sort()
	return (wordList == user)

# Takes sorted input, filters words to words of same length
# loops over filtered words and uses isAnAnagram function
def getAnagrams(user):
	lister = [word for word in words if len(word) == len(user) ]
	for item in lister:
		if isAnAnagram(item, user):
			yield item

# Another method of returning a list  similar to original getAnagrams
# Uses filter and a lamda expression to filter all words in the list that are 
# anagrams of the sorted word. Should be slower.
def getAnagrams2(user):
	lister = [word for word in words if len(word) == len(user) ]
	anagrams = list( filter((lambda x:isAnAnagram(x,user)), lister))
	return anagrams

# Shuffles user input once only
# Returns sorted list
def sortInput(user):
	wet = list(user)
	wet.sort()
	return wet

def test():
	a = sortInput('andrew')
	getAnagrams(a)

def test2():
	a = sortInput('andrew')
	getAnagrams2(a)


# reads from files to list and closes file
#  Used the f.closed print to demonstrate
# fact that with keyword executes block, closes file but
# results in an object i.e. f is available outside block
# Easily demonstrated by running script in ipython where when
# exited  f can still be accessed by typing f
with open('wordlist.txt', 'r') as f:
	allwords = f.readlines()
print(f.closed)

# Creates a list of words from the files
# Strips new
for x in allwords:
	x = x.rstrip()
	words.append(x)
inp = 1

# Takes input
# while inp != "99":
# 	inp = input("enter word:")
# 	blah = sortInput(inp)
# 	result = getAnagrams(blah)
# 	print(list(result))
# 	print(getAnagrams2(blah))





#Fin
