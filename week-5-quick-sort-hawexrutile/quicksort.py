# Creating a list of 10 random integers. 
import random

min = 9
max = 99
count = 10

RandomListOfIntegers = [random.randint(min, max) for iter in range(count)]

print(RandomListOfIntegers)

# Code for Quick Sort here 
def partition(list,l,h):
	pivot=list[h]
	i=l-1
	for j in range(l,h):
		if pivot>list[j]:
			i=i+1
			list[i],list[j]=list[j],list[i]
	
	list[h],list[i+1]=list[i+1],list[h]
	return i+1
def quicksort(list,l,h):
	if l<h:
		q=partition(list,l,h)
		quicksort(list,l,int(q)-1)
		quicksort(list,int(q)+1,h)

quicksort(RandomListOfIntegers,0,len(RandomListOfIntegers)-1)
print (RandomListOfIntegers)
	
