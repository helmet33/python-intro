# Taken almost verbatim from: http://www.quickperm.org/
def anagrams(word):
  p = list(range(len(word) + 1))
  i = 1
  # Word has to be mutable.
  word = list(word)

  while i < len(word):
    gj = p[i]-1
    print("%(a)d swapped become %(b)d" %{"a":p[i] ,"b":gj})

    p[i] = p[i] - 1

    if i % 2 == 1:
      j = p[i]
    else:
      j = 0

    word[i], word[j] = word[j], word[i]

    i = 1
    while p[i] == 0:
      p[i] = i
      i = i + 1
    print(p)

    yield "".join(word)


word = "abcd"
i = 1

print("The anagrams of %s are:" % word)
print(word)
for anagram in anagrams(word):
  i = i + 1
  print(anagram)

print("There are %d anagrams in total." % i)
