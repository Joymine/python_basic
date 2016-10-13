 # -*- coding: utf-8 -*-
 #上面的一行添加，标识编码，否则出现中文报错
print "=======================fileter===================="
# filter(fuc_var,list)  return true/false  ,if func_var is true ,then keep the item,otherwise delete the item of the given list

def is_prime(x):

	if type(x) == type(1):
		if x <= 2:
			return False
		for i in range(2,x-1):
			if x % i ==0 :
				return True
	return False

#is_prime can be inproved
#print is_prime(6) test use

num_to_judge = input("input a num :")
list = range(1,num_to_judge)
print filter(is_prime,list)

print "=======================sorted===================="
#sorted(list,key=func)  按照func的方法来排序

#输入一组学生

L = []
name = raw_input("input name :")
score = input("input score :")

while name!="over":
	st = name,score
	L.append(st)
	name = raw_input("input name :")
	score = input("input score :")

