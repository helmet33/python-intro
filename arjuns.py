##Arjun Kharel - Software Development (GMIT) - Theory of Algorithms
import sys
import os

wordmap = dict()

def anagram(word):
	#convert to ascii value first and check against the dict words
	convertedKey = sum(bytearray(word,'utf8'))

	#print ("ASCII value of %s, is %d" % (word,convertedKey))

	if(convertedKey in wordmap):
		templist = wordmap.get(convertedKey)
		#result = [s for s in templist if not s.strip(word)]
		result = [s for s in templist if sorted(word)==sorted(s)]
		if (result):
			print ("List of Anagram's:\n %s" %(result))
		else:
			print("No anagram found  for: " + word + ",not found in the dictionary...")

	else:
		print("No anagram found  for: " + word + ",not found in the dictionary...")

def addToMap(key,value):
	if key in wordmap:
		wordmap.get(key).append(value) #if key exists, get the reference to the list(value) and add it.
	else:
		wordmap.update({key:[value]})

def preprocessing():
	print("pre processing")

	wordsList = [line.rstrip('\n') for line in open('wordlist.txt')]
	for word in wordsList:
		#generate the key #generate the value
		key = sum(bytearray(word,'utf8')) #sum of the word, ascii value
		addToMap(key,word)

#calling the function
def beginProcess():
	preprocessing()
	word = input("Enter your word to get anagrams or 0 to exit:")
	while(word!="0"):
		anagram(word) #example: chaoatiricatrezn --> characterization
		word = input("Enter your word to get anagrams or 0 to exit:")

beginProcess()

## some of the code snippets was taken from
##http://stackoverflow.com/questions/3277503/python-read-file-line-by-line-into-array
##http://stackoverflow.com/questions/8452961/convert-string-to-ascii-value-python