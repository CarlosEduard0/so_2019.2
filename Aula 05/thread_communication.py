
import threading
import time
import os

var1 = 0
var2 = 0

def thread_func1():
	self_t = threading.currentThread()
	while True :
		print ("Sou o processo " + str(os.getpid()) + " na thread " + str(self_t.ident))
		print ("Valor de Var1 " + str(var1))
		time.sleep(1)

def thread_func2():
	self_t = threading.currentThread()
	while True :
		print ("Sou o processo " + str(os.getpid()) + " na thread " + str(self_t.ident))
		print ("Valor de Var2 " + str(var1))
		time.sleep(1)


t1 = threading.Thread(target=thread_func1, args=())
t2 = threading.Thread(target=thread_func2, args=())
t1.start()
t2.start()
while True :
	print ("Sou o processo principal " + str(os.getpid()) + " estou executando em paralelo às trhreads" + str(t1.ident) + " e " + str(t2.ident))
	var1 = var1 + 1
	var2 = var2 + 1
	time.sleep(1)

#
