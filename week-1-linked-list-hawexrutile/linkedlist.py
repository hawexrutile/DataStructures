
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
	def mid(self,value,position):
		box3=Box(value)
		pointer=self.head
		n=2
		while n!=position:
			n+=1 
			pointer=pointer.next
		box3.next=pointer.next
		pointer.next=box3
	def end(self,value):
		box2=Box(value)
		pointer=self.head
		while pointer.next!=None:
			pointer=pointer.next
		pointer.next=box2
		
	def rfront(self):
		self.head=self.head.next
	def rmiddle(self,info):
		pointer=self.head
		while pointer!=None:
			if pointer.next.data==info:
				pointer.next=pointer.next.next
				break
			else:
				pointer=pointer.next
	def rend(self):
		pointer=self.head
		while pointer.next.next!=None:
			pointer=pointer.next	
		pointer.next=pointer.next.next
	def length(self):
		pointer=self.head
		n=0
		while pointer!= None:
			n+=1
			pointer=pointer.next
		print (n)
	def position(self,info):
		pointer=self.head
		n=1
		while pointer.data!=info:
			n+=1
			pointer=pointer.next
		print (n)
	def search(self,info):
		pointer=self.head
		while pointer != None:
			if pointer.data==info:
				print ("it's here")
			elif pointer.next!=None:
				pointer=pointer.next
			else :
				print ("it's not here")
				break
	def display(self):
		pointer=self.head
		while pointer!=None:
			print (pointer.data)
			pointer=pointer.next
	def reverse(self):
		pointer=self.head
		while pointer!=None:
			a.begin(pointer.data)
			a.rmiddle(pointer.data)
			pointer=pointer.next
a=Linking()
a.begin("alan")
a.begin("kd")
a.begin("ajay")
a.end("Jinan")
a.mid("Ashwin",2)
a.position("alan")
a.search("lol")
a.rmiddle("kd")
a.rfront()
a.rend()
a.reverse()
a.display()

