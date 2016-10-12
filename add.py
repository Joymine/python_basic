


def fact(i):
	if i <= 1:
		return i;
	else :
	    return i * fact(i-1)


def run_me_once():
	#n = input()   #NOK  input() will return a str,it will reports :unorderable types
	n = int(input("please input a num:"))
	result = fact(n)
	#print result   ==ERROR,need brackets 
	print (result)  #OK
	



m=input("please input a num:")
print(m)

while m!='\\':
	mm= int(m)
	result = fact(mm)
	print('result is : ',result)
	m= input('input a new num :')
    
 

	