# -*- coding: utf-8 -*-
import signal
import time
import os
#exemplo para ser usado com system

def handler(signum, arg):
	print('Parando de executar...')
	os.kill(os.getpid(), signal.SIGSTOP)

def handler2(signum, arg):
	print('Voltando a executar...')

signal.signal(signal.SIGUSR1, handler)
signal.signal(signal.SIGCONT, handler2)

print (os.getpid())
while True:
	print ('programa rodando em loop')
	time.sleep(1); #espera por 1 segundo

print ('Se chegar aqui podemos estar com problema')
