import string
def string_operation():
	myfile = open()
	pun = string.punctuation
	his = dict()
	counter = 0
	listofwords = []
	for my in mylife:
		my=my.strip()
		for c in pun:
			my = my.replace(c,"")
		my = my.lower()
		lis = my.split()
		for li i n lis:
			listofwords.append(li)
	for lists in listofwords:
		if lists not in his:
			his[lists] = 1
		else:
			his[lists] += 1
	for key,value in his.items():
		if(value == 20):
		print(key)

string_operation()
