import threading
import time

var = 0

def thread_par():
    global var
    while True:
        if var % 2 == 0 and var > 0:
            var = var - 1

def thread_impar():
    global var
    while True:
        if var % 2 != 0 and var > 0:
            var = var + 1

thread1 = threading.Thread(target = thread_par, args = ())
thread2 = threading.Thread(target = thread_impar, args = ())
thread1.start()
thread2.start()

while True:
    var = var + 2
    print("Valor anterior da variável " + str((var - 2)) + ", valor após incremento " + str(var))
    time.sleep(1)