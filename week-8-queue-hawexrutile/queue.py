class Box():
	def __init__(self,data):
		self.data=data
		self.next=None
class Queue():
	def __init__(self):
		self.head=None	
	def enqueue(self,value):
		if a.size()<4:
			NewBox=Box(value)
			NewBox.next=self.head
			self.head=NewBox
		else:
			print"Queue is full ,cant add elements:Overflow"
	def display(self):
		pointer=self.head
		while pointer!=None:
			print pointer.data
			pointer=pointer.next

	
	def dequeue(self):
		if a.size()>1:
			if self.head.next.next!=None:
				pointer=self.head
				while pointer.next.next!=None:
					pointer=pointer.next	
				pointer.next=pointer.next.next
		elif self.head==None:
			print "cant remove elemets as queue is empty:Underflow"
		else:
			self.head=None
		
	def front(self):
		pointer=self.head
		if self.head!=None:
			while pointer.next!=None:
				pointer=pointer.next
			print "The front most element is",pointer.data
		else:
			print"The is empty and hence no frontmost element"
	def rear(self):
		if self.head!=None:
			print "The list rear element in the queue is",self.head.data
		else:
			print"The list is empty and hence no rear element"
	def size(self):
		pointer=self.head
		n=0
		while pointer!= None:
			n+=1
			pointer=pointer.next
		return n

a=Queue()
a.enqueue("alan")
a.enqueue("kd")
a.enqueue("ajay")
a.enqueue("Jinan")
a.enqueue("Ashwin")
a.dequeue()
a.dequeue()
a.front()
a.rear()
a.display()
