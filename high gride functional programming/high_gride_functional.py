 # -*- coding: utf-8 -*-
 #上面的一行添加，标识编码，否则出现中文报错
#Higher-order function


print"==================function as param  BEGIN 中文测试=================="
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
	#print str.upper()
	#print str.title()
	#print str.lower()
	#print str.capitalize()
	return str.upper()

def toString(name,f):
	return f(name)


#source = input("input a string :") NOK,because input will return a num
#source = raw_input("input a string :")
#result = toString(source,turn_UPPER)
#print "you expcet answ :",result

list=[]
str = raw_input("input a str :")
while str!= 'ok':
	list.append(str)
	str = raw_input("input a str :")

print "result is :"
print map(turn_UPPER,list)

list_num = []
num = input("input a num :")
while num!=0:
	list_num.append(num)
	num = input("input a num :")

def cub(x,y):
	return x * y

print reduce(cub,list_num)



