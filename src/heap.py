
class  Heap(object, arr):
	"""docstring for  heap"""
	def __init__(self, arr):
		self.heap=arr
		self.buildMinHeap(self.heap)
		
	def parent(self,index):

		return index/2

	def left_child(self,index):

		return 2*index+1

	def right_child(self,index):

		return 2*index+2

	def heapify(self, index):
		""" Create heap again """

		left_index=self.left_child(index)
		right_index=self.right_child(index)
		minimum=index
		heap_len=len(self.heap)
		if right_index <heap_len and self.heap[right_index]<self.heap[index]:
			minimum=right_index
		if left_index<heap_len and self.heap[left_index]<self.heap[index]:
			minimum=left_index
		if minimum!=index:
			self.heap[index], self.heap[minimum] = self.heap[minimum], self.heap[index]
			self.heapify(minimum)

		return

	def buildMinHeap(self):
		for i in range(len(self.heap),-1,-1):
			self.heapify(i)
		return
	def heappop(self):
		"""pop the element from head"""
		return
	def heappush(self.heap,):
		"""Insert on heap  """

		return
		
if __init__=='main':
	arr=[2,3,7,4,9,0]
	H=Heap(arr)
	print 