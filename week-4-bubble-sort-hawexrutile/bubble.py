
# Creating a list of 10 random integers. 
import random

min = 9
max = 99
count = 10

RandomListOfIntegers = [random.randint(min, max) for iter in range(count)]

print(RandomListOfIntegers)

# Code for Bubble Sort here 
def BubbleSort(inputlist):
	i=0
	while i!=len(inputlist)+1:
		i=i+1
		for a in range(0,len(inputlist)-1):
			if inputlist[a]>inputlist[a+1]:
				inputlist[a],inputlist[a+1]=inputlist[a+1],inputlist[a]
	print (inputlist,"is ur sorted list")
BubbleSort(RandomListOfIntegers)
