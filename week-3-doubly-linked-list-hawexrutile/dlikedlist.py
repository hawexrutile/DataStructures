class Box:
	def __init__(self,data):
		self.data=data
		self.next=None
		self.prev=None
class Dlinkedlist:
	def __init__(self):
		self.head=None
	def begin(self,value):
		box1=Box(value)
		box1.next=self.head
		if self.head!=None:
			self.head.prev=box1
			box1.next=self.head
		self.head=box1

	def mid(self,value,position):
		box3=Box(value)
		pointer=self.head
		n=0
		while n!=position-2:
			n+=1
			pointer=pointer.next
		box3.next=pointer.next
		box3.prev=pointer
		pointer.next.prev=box3
		pointer.next=box3
	
	def end(self,value):
		box2=Box(value)
		pointer=self.head
		while pointer.next!=None:
			pointer=pointer.next
		pointer.next=box2
		box2.prev=pointer
		box2.next=None
		
	def rfront(self):
		self.head=self.head.next
	def rmiddle(self,info):
		pointer=self.head
		while pointer.next!=None:
			if pointer.next.data==info:
				pointer.next=pointer.next.next
				break
			else:
				pointer=pointer.next
	def rend(self):
		pointer=self.head
		while pointer.next!=None:
			pointer=pointer.next	
		pointer.prev.next=pointer.next
	def reverse(self):
		pointer=self.head
		while pointer!=None:
			a.begin(pointer.data)
			a.rmiddle(pointer.data)
			pointer=pointer.next			
	def display(self):
		pointer=self.head
		while pointer!=None:
			print (pointer.data)
			pointer=pointer.next
	def search(self,info):
		pointer=self.head
		while pointer != None:
			if pointer.data==info:
				print ("it's here")
				break
			elif pointer.next!=None:
				pointer=pointer.next
			else :
				print ("it's not here")
				break
	def possition(self,info):
		pointer=self.head
		n=1
		while pointer!=None:
			if pointer.data!=info:
				n+=1
				pointer=pointer.next
				
			else:
				print (n)
				break
	
a=Dlinkedlist()
a.begin("kd")
a.begin("shwe")
a.begin("ajay")
a.begin("anand")
a.end("alan")
a.mid("dundu",4)
a.rend()	
a.rmiddle("shwe")
a.rfront()
a.possition("dundu")
a.search("dundu")
a.display()
a.reverse()
a.display()
