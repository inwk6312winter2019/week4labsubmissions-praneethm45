import string 
def rm_pattern(word):
 pun = string.punctuation
 str = ""
 for s in pun:
  str = word.strip()
  str = word.replace(s,'')
  return str

def vp(f1,f2):
 try:
 master = open(file1,"r")
 slave = open(file2,"w")
  for m in master:
   new = remove_pattern(master)
   slave.write(master)
		print("success")
	except:
		print("!!!!!!!!!!!!!!!!!!")

x =input("enter master file for copy operation")
y = input("enter slave file")
sed(x,y)
