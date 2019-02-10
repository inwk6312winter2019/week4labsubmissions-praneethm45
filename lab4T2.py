import string

fp=open('batman.txt')
name=fp.read()
for line in name.split():
	word=line.strip(string.punctuation)
print(word.lower())
