class Kangaroo:
	"""A Kangaroo is a marsupial."""
	def __init__(self, name, contents=None):
        	"""Initialize the pouch contents.
		name: string
        	contents: initial pouch contents.
        	"""
        	self.name = name
        	self.pouch_contents = contents or []

	def __str__(self):
        	"""Return a string representaion of this Kangaroo.
        	"""
        	t = [self.name + ' has pouch contents:']
        	for obj in self.pouch_contents:
            		s = ' ' + object.__str__(obj)
            		t.append(s)
        	return '\n'.join(t)

	def put_in_pouch(self, item):
        	"""Adds a new item to the pouch contents.
        	item: object to be added
        	"""
        	self.pouch_contents.append(item)

kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
roo.put_in_pouch(roo)
roo.put_in_pouch('new car keys')
roo.put_in_pouch('new function call')


print(kanga)
print(roo)
