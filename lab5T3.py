class Time:
	"""this class represents time"""

	"""def print_time(self,t):
		print('the time is:','%.2d:%.2d:%.2d'%(t.hour,t.minute,t.second))"""

time=Time()
time.hour=9
time.minute=35
time.second=25
def print_time(t):
	print('the time is:','%.2d:%.2d:%.2d'%(t.hour,t.minute,t.second))

print_time(time)
