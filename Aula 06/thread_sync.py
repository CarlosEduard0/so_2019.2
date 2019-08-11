
import threading
import time
import os

var = 10
lock = threading.Lock()
lock2 = threading.Lock()

def thread_func():
	global var
	global lock
	self_t = threading.currentThread()
	while True :
		print ("Sou o processo " + str(os.getpid()) + " na thread " + str(self_t.ident))
		#regiao crítica, precisa ler e escrever o valor de val
		lock.acquire()
		print ("Valor de Var " + str(var))
		var = var + 1
		lock.release()
		#fim da regiao crítica
		time.sleep(1)

def thread_func2():
	global var
	global lock2
	self_t = threading.currentThread()
	while True :
		print ("Sou o processo " + str(os.getpid()) + " na thread " + str(self_t.ident))
		#regiao crítica, precisa ler e escrever o valor de val
		lock2.acquire()
		print ("Valor de Var " + str(var))
		var = var + 1
		lock2.release()
		#fim da regiao crítica
		time.sleep(1)


t1 = threading.Thread(target=thread_func, args=())
t2 = threading.Thread(target=thread_func2, args=())
t1.start()
t2.start()
while True :
	print ("Sou o processo principal " + str(os.getpid()) + " estou executando em paralelo às trhreads" + str(t1.ident) + " e " + str(t2.ident))
	#regiao crítica, precisa ler e escrever o valor de val
	lock.acquire()
	lock2.acquire()
	var = var+1;
	lock.release()
	lock2.release()
	#fim da regiao crítica
	time.sleep(1)

#
