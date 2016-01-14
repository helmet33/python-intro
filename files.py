f = open('wordlist.txt', 'r')
o = open('amended.txt', 'w+')
i = 0
for i in range(0,10,1):
	a = f.readline()
	o.write(a)
f.close()
o.close()
o = open('amended.txt', 'r')
words = o.readlines()

for w in words:
	print(w.rstrip())
