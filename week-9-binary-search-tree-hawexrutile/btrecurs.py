class Box:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
		self.parent=None
class BinarysearchT:
	def __init__(self):
		self.root=None
	def searchvalue(self,dad,value):
		pointer=dad
		if pointer.data==value or pointer==None:
			return pointer
		elif pointer.data<value:
			return self.searchvalue(pointer.right,value)
		else:
			return self.searchvalue(pointer.left,value)
	def search(self,value):
		a=self.searchvalue(self.root,value)
		if a.data==None:
			print ("its not here")
		else :
			print ("its here"),a.data
	def insert(self,value):
		b=Box(value)
		a=self.insertvalue(self.root,value)	
		if self.root==None:
			self.root=b
		
		elif a.data<value:
			b.parent=a
			a.right=b
		elif a.data>value:
			b.parent=a
			a.left=b
		else:
			print ("cant add")
			
	def insertvalue(self,dad,value):
		pointer=dad
		if pointer!=None:
			if pointer.data<value and pointer.right!=None:
				return self.insertvalue(pointer.right,value)
			elif pointer.data>value and pointer.left!=None:
				return self.insertvalue(pointer.left,value)
			else:
				return pointer
	def remove(self,value):

		a=self.searchvalue(self.root,value)
		s=self.suc(a)
		if s!=None:
			s.parent==a.parent
			s.left==a.left
			s.right=a.right
			
		if a.parent!=None:
			if a.parent.left==a:
				a.parent.left=s
			else:
				a.parent.right=s
	def suc(self,value):
		if value.left!=None:
			z=self.max(value.left)
			if z.left!=None:
				z.parent.right=z.left
				z.left.parent=z.parent
				z.left=None
			return z	
				
		elif value.right!=None:
			z=self.min(value.right)
			if z.right!=None:
				z.parent.right=z.right
				z.right.parent=z.parent
				z.right=None
			return z
		else :
			return None
	def min(self,value):
		if value.left==None:
			return value
		else:
			return self.min(value.left)
	def max(self,value):
		if value.right==None:
			return value
		else:
			return self.max(value.right)

	def in_order(self,dad):
		if dad!=None:
			self.in_order(dad.left)
			print (dad.data)
			self.in_order(dad.right)
	def display(self):
		self.in_order(self.root)
	
	def test(self):
		print (self.searchvalue(self.root,10).parent.data)
		print (self.searchvalue(self.root,32).parent.data)
		print (self.searchvalue(self.root,99).parent.data)
		print (self.searchvalue(self.root,56).parent.data)
		print (self.searchvalue(self.root,15).parent.data)
		print (self.searchvalue(self.root,13).parent.data)
		print (self.searchvalue(self.root,78).parent.data)
	
a=BinarysearchT()
a.insert(5)
a.insert(10)
a.insert(32)
a.insert(99)
a.insert(56)
a.insert(15)
a.insert(13)
a.insert(78)
a.insert(7)
a.remove(56)
a.display()		
#a.test() 