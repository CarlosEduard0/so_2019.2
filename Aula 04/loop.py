# -*- coding: utf-8 -*-
import signal
import time
import os
#exemplo para ser usado com system

def handler(signum, arg):
	print('recebi usr1, vou pausar')
	os.kill(os.getpid(), signal.SIGSTOP)

signal.signal(signal.SIGUSR1, handler)

print (os.getpid())
while True:
	print ('programa rodando em loop')
	time.sleep(1); #espera por 1 segundo

print ('Se chegar aqui podemos estar com problema')
