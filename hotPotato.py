from pyQueue import Queue

def hotPotato(namelist, num):
	simqueue = Queue()
	for name in namelist:
		print(name)
		simqueue.enqueue(name)

	while simqueue.size() > 1:
		for i in range(num):

			a = simqueue.peek()
			print("Sent",a,"to front!")
			simqueue.enqueue(simqueue.dequeue())
			print("------------------------")
			
		a = simqueue.peek()
		simqueue.dequeue()
		print("Now i dequeued",a)
		print("===========================")
		
	print("Now i am returning ",simqueue.peek())
	return simqueue.dequeue()
				
print(hotPotato(["Aung Aung", "Mg Mg" , "Thiha" , "Thin Thin" , "Ko Ko" , "Hla Hla"],8))