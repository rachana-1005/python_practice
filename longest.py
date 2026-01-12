#24.Longest word:
sentence="I love Python programming"
words=sentence.split()
longest=0
for w in words:
    if len(w)>longest:
        longest=len(w)
print("Longest word length:",longest)
