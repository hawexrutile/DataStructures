class Box():
	def __init__(self,data):
		self.data=data
		self.next=None
class Linking():
	def __init__(self):
		self.head=None	
	def begin(self,value):
		NewBox=Box(value)
		NewBox.next=self.head
		self.head=NewBox
		
		if self.head.next==None:
			self.head.next=self.head
		else:	
			pointer=self.head.next
			while pointer.next!=self.head.next:
				pointer=pointer.next
			pointer.next=self.head

	def display(self):
		pointer=self.head
		while pointer.next!=self.head:
			print (pointer.data)
			pointer=pointer.next
		print (pointer.data)
	def end(self,value):
		box2=Box(value)
		pointer=self.head
		while pointer.next!=self.head:
			pointer=pointer.next
		box2.next=self.head
		pointer.next=box2
		
	def mid(self,value,position):
		box3=Box(value)
		pointer=self.head
		n=0
		while n!=position-2:
			n+=1
			pointer=pointer.next
		box3.next=pointer.next
		pointer.next=box3

	
	def search(self,info):
		pointer=self.head
		if self.head.data==info:
			print ("it's here")
			print ("and its possition is : 1")
		else:
			n=1
			while pointer.next != self.head:
				if pointer.data==info:
					print ("it's here")
					print ("and its possition is : "+str(n))
					break
					
				else :
					n+=1
					pointer=pointer.next
	def rfront(self):
		
		pointer=self.head
		while pointer.next!=self.head:
			pointer=pointer.next
		pointer.next=self.head.next
		self.head=self.head.next
	def rmiddle(self,info):
		pointer=self.head
		while pointer.next!=self.head:
			if pointer.next.data==info:
				pointer.next=pointer.next.next
				break
			else:
				pointer=pointer.next
	def rend(self):
		pointer=self.head
		while pointer.next.next!=self.head:
			pointer=pointer.next
				
		pointer.next=self.head
	def reverse(self):
		pointer=self.head
		while pointer.next!=self.head:
			a.begin(pointer.data)
			a.rmiddle(pointer.data)
			pointer=pointer.next
			a.begin(pointer.data)
			a.rmiddle(pointer.data)
                        

a=Linking()
a.begin("alan")
a.begin("kd")
a.begin("ajay")
a.end("Jinan")
a.mid("Ashwin",2)
a.display()
a.search("alan")
a.rfront()
a.rmiddle("alan")
a.rend()
a.reverse()
a.display()
		

		
                                 

