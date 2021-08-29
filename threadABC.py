import time
import threading

def a():
	print("A")
	return
def b():
	print("B")
	return
def c():
	print("C")
	return

t1 = threading.Thread(target=a)
t2 = threading.Thread(target=b)
t3 = threading.Thread(target=c)

t1.start()
t3.start()
t2.start()