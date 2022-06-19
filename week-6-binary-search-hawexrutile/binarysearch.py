
a=range(1,10)
def binarysearch(value,list,lower,higher):
	b=(higher+lower)//2
	if b>len(list):
		print "the given element is not present in the list"
	elif b<1:
             	print "the given element is not present in the list"
	elif lower<higher :
                if value<list[b-1]:
                        binarysearch(value,list,lower,b-1)
                elif value>list[b-1]:
                        binarysearch(value,list,b+1,higher)
                elif value==list[b-1]:
                      	print "The element:",value," is here and it is in the",b," th position"

	else:
             	print "the given element is not present in the list"

binarysearch(100,a,1,10)

