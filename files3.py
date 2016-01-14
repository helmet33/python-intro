f = open('wordlist.txt', 'r')
o = open('appended3.txt', 'w')
words = []
i = 0
allwords = f.readlines()
f.close()
for x in allwords:
	if len(x) == 4:
		words.append(x)
for x in range(10):
	a = words[x]
	print(a.rstrip())
	o.write(a)
o.close()

