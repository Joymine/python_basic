classmate = ["joymine","Tom","Jack","Bill","Yoyo"]




print "====================slice BEGIN ============================="
print("classmate   is : ",classmate)
print "classmate[-1] is : ",classmate[-1] #   Yoyo
print "classmate[:2] is : ",classmate[:2] #   ['joymine', 'Tom']
print "classmate[-2:] is : ",classmate[-2:] #   ['Bill', 'Yoyo']
#c= classmate[-4:] 
#print "c :",c
#print "c[2] is : ",classmate[2] # 
print "classmate[:4:2] is : ",classmate[:4:2] #   ['joymine', 'Jack']
print "classmate[::2] is : ",classmate[::2] #  ['joymine', 'Jack', 'Yoy


print "====================Iteration BEGIN ============================="
for i, value in enumerate(['A', 'B', 'C']):   #enumerate usage
	print i,value
#print "Judge classmate interable : "
#isi = isinstance(classmate ,Iterable )   Can not work  ,NOK


print "====================List Comprehensions BEGIN ============================="

print range(1,10)

List1 = []
for x in range(1,10):
	List1.append(x*x)
print List1

#above equals as below  List1 == List2

List_2 = [x*x for x in range(1,10)]
print List_2

#strs = [ m + n for m in [['A','B'],['a','b']] NOK
# print strs  NOK

print "====================List Comprehensions BEGIN ============================="
print "Fibonacci calculate :"
def febr(x):
	#L = []
	n,a,b = 0,0,1
	while n < x:
		#L.append(b)
		yield b
		a,b=b,a+b
		n = n + 1
	print L

ooo = febr(int(input('input a umm :')))
ooo.next() #NOK  NOT tatally understood