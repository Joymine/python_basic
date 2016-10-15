


def add(x,y):
	return x+y

def sub(x,y):
	return x-y

def ab(x,y):
	return x*y

def func_as_parm(x,y,f):
	return f(x,y)

class Calculate(object):
	"""docstring for Calculate"""
	def __init__(self, x,y,func):
		super(Calculate, self).__init__()
		self.func = func
		self.x = x
		self.y = y
    
	def work_out(self):
		return self.func(self.x,self.y)


class Calculate_info(Calculate):
	pass



#initialize 
cal = Calculate_info(4,5,ab)
#cal.print_info()
result = cal.work_out()
print(result)


		