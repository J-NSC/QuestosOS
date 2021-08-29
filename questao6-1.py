import threading
import time

tempo = 0
cont = 0

while (cont < 20):
	def a():
		print('ABC')
		return 0
	ini = time.time()
	t1=threading.Thread(target=a)
	t1.start()
	fim = time.time()

	temp = fim-ini
	tempo = tempo+temp
	cont = cont + 1

print ("tempo medio thread:", tempo/20)