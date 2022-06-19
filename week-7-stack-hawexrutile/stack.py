class Box():
	def __init__(self,data):
		self.data=data
		self.next=None
class stacking():
	def __init__(self):
		self.head=None	
	def push(self,value):
		NewBox=Box(value)
		NewBox.next=self.head
		self.head=NewBox
	def display(self):
		pointer=self.head
		while pointer!=None:
			print pointer.data
			pointer=pointer.next
	def empty(self):
		if a.size()==0:
			print "list is empty"
		else :
			print "list is not empty"

	def size(self):
		pointer=self.head
		n=0
		while pointer!= None:
			n+=1
			pointer=pointer.next
		return n
	def top(self):
		if a.size()!=0:
			print "the top element is",self.head.data
			print "and its is the",a.size(),"th element from botom"
		else :
			print "their is no top element as the stack is empty"
	def pop(self):
		self.head=self.head.next



a=stacking()
a.push("alan")
a.push("kd")
a.push("ajay")
a.push("Jinan")
a.push("Ashwin")
a.pop()
a.pop()
a.top()
print(a.size())
a.display()
a.empty()
