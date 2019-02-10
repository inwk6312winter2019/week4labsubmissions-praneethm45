from math import sqrt
class point:

	def dist_between_points(self,a,b):
		dx=a
		dy=b
		print(a.x,b.x)
		dx=a.x-b.x
		dy=a.y-b.y
		print(dx,dy)
		dist=sqrt(dx**2+dy**2)
		print(dist)

p1=point()
p2=point()
p1.x=5
p2.x=4
p1.y=6
p2.y=4

p1.dist_between_points(p1,p2)

