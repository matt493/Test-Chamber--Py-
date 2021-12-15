
"""
alienList is a list sent by alien mothership.
retM is number of elements of the list returned by Earth.
"""
from operator import itemgetter

class msg:
	def __init__(self,val,key):
		self.val = val
		self.key = key

def decToBin(n):
	return bin(n).replace("0b","")
	
def retStream(alienList, retM):
	lst=list()
	counter = dict()
	for each in alienList:
		bin_val = str(decToBin(each))
		counter[each]=bin_val.count('1')

	counter=dict(reversed(sorted(counter.items(),key=itemgetter(1))))
	
	key_lst = list()
	val_lst = list()
	
	for k,v in counter.items():
		key_lst.append(k)
		val_lst.append(v)
			
	key_lst.reverse()
	val_lst.reverse()
	
	for i,j in enumerate(val_lst):
		print(i,j)
	return counter

def main():
	# input for alienList
	alienList = [1,2,3,4,5]
	alienList_size  = 5
	# input for retM
	retM = 3
	
	result = retStream(alienList, retM)
	# print(" ".join([str(res) for res in result]))	

if __name__ == "__main__":
	main()