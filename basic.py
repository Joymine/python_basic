classmate = [3,5,4]
classmate.append(1)
print classmate
print (' bubble sort')


for x in range(len(classmate)):
	for y in range(len(classmate)-x-1):
		if classmate[y] < classmate[y+1] :
			temp= classmate[y]
			classmate[y] =classmate[y+1]
			classmate[y+1] = temp
		  		

print("end for")
print classmate