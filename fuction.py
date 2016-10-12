def bubble_sort(classmate=[]) :
	print (' bubble sort begin>>>>>>>>>>>')
	for x in range(len(classmate)):
		for y in range(len(classmate)-x-1):
			if classmate[y] < classmate[y+1] :
				temp= classmate[y]
				classmate[y] =classmate[y+1]
				classmate[y+1] = temp
	print (' <<<<<<<<<<bubble sort end')
	return classmate


#insert will append every time,EX  3,5,4,2;  3,5,4,2,2;  ...
def insert (L=[]):
	L.append(2)
	print classmate
	return L

#insert will append every time,EX  3,5,4,2;  3,5,4,2,2;  ...


#insert just append once ,EX 3,5,4,2;  3,5,4,2;  ...
def insert_static(L=None):
	if L is None :
		L = []
		L.append(2)
		print L
        return L


classmate = [3,5,4]
#classmate.append(1)
#print classmate
#bubble_sort(classmate)
#print classmate

insert_static(classmate)

insert()
insert()

