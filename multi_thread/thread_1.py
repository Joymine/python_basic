
#-*- encording:utf-8 -*-
from multiprocessing import Process
import os
#print ("测试")
#print("Process (%s) is starting...."%os.getpid())


def ab(name):
	print("run child process %s id %s"%(name,os.getpid()))

if __name__ == "__main__":
	print("parent process %s ."%os.getpid())
	p =Process(target = ab,args=('test'))
	print("child process BEGIN----")
	p.start()
	p.join()
	print("child process END......")
