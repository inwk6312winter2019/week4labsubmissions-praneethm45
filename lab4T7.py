import hashlib
import os

def md5(fname):
	hash_md5 = hashlib.md5()
	with open(fname,"rb") as f:
		for chunk in iter(lambda: f.read(8084),b""):
			hash_md5.update(chunk)
	return hash_md5.hexdigest()

PATH = os.getenv("HOME")
def findfile(extension):
	for root,subFolder,files in os.walk(PATH):
		for item in files:
			if item.endswith("'"+str(extension)):
				fileNamePath = str(os.path.join(room,item))
				print(fileNamePath," ",md5(fileNAmePath))

x = input("enter file extension for search operation:")
findfile(x)
