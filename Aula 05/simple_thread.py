
import threading
import time
import os

def thread_func(argumentos):
	t = threading.currentThread()
	while True :
		print("Argumentos recebidos: " + argumentos)
		print ("Sou o processo " + str(os.getpid()) + " na thread " + str(t.ident))
		time.sleep(1)


x = threading.Thread(target=thread_func, args=("Novo",))
x.start()
while True :
	print ("Sou o processo principal " + str(os.getpid()) + " estou executando em paralelo a trhread" + str(x.ident))
	time.sleep(1)

# x.join()
