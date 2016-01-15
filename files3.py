# Function to check if the word is an anagram
def isAnAnagram(word, user):
    wordAsList= list(word)
    wordAsList.sort()
    inputAsList= list(user)
    inputAsList.sort()

    return (wordAsList == inputAsList)

with open('wordlist.txt', 'r') as f:
	allwords = f.readlines()
f.close()

words = []
for x in allwords:
	x = x.rstrip()
	words.append(x)


inp = input("enter word:")
lister = [word for word in words if len(word) == len(inp) ]
for item in lister:
	if item != inp:
		if isAnAnagram(item, inp):
			print(item)

#print(lister)
