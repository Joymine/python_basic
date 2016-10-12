#Higher-order function


print"==================function as param  BEGIN =================="
def add(x,y):
	return x+y

def sub(x,y):
	return x-y

def ab(x,y):
	return x*y

def func_as_parm(x,y,f):
	return f(x,y)
print func_as_parm(3,4,sub)
print func_as_parm(3,4,add)
print func_as_parm(3,4,ab)

print"================== map / reduce  BEGIN =================="
print "if you want to know more,please refer to   research.google.com/archive/mapreduce.html"
# build-in function   map(function_var,list)  the param function_var will operate each item in list,@return a new list

def turn_UPPER(str):
	print str.upper()
	print str.title()
	print str.lower()
	print str.capa
	return str.upper()

