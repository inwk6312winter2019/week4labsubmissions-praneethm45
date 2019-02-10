import copy

class point:
	"""this class represents point"""

class rectangle:
	"""this class represents a rectangle"""

	def find_center(self,rect):
	        p = point()
       		p.x = rect.corner.x + rect.width/2
        	p.y = rect.corner.y + rect.height/2
        	return p

	def print_point(self,p):
	        print('(%g,%g)'%(p.x,p.y))

	def move_rectangle(self,rect,dx,dy):
		rect.width += dx
		rect.height += dy

box=rectangle()
box.width=100.0
box.height=200.0
box.corner=point()
box.corner.x=0.0
box.corner.y=0.0
box2=copy.deepcopy(box)

center=box.find_center(box)
box.print_point(center)
box.move_rectangle(box,70,120)
print(box.width,box.height)
box2.move_rectangle(box2,90,140)
print(box2.width,box2.height)

