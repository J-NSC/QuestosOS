import os
import time

tempo = 0
cont = 0

while (cont < 20):
	def parent_child_process():
		n = os.fork()

		if n==0:
			print('ABC')
			os._exit(0)
			
	ini = time.time()
	parent_child_process()
	fim = time.time()

	temp = fim-ini
	tempo = tempo+temp
	cont = cont + 1

print ("tempo medio processo	:", tempo/20)