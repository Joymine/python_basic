'module'
__author__ = 'joynmine'

import sys
def _say_hi(name):
	print("hi ,%s"%name)

def _say_hello(name):
	print("hello,%s"%name)

def say_hello():
	args = sys.argv
	if len(args) >=1:
		if len(args[1])>5:
			_say_hello(args[1])
		else:
			_say_hi(args[1])
	#print (sys.path())
	#print ("hello,",args[1])



if __name__ == '__main__':
	say_hello()