
		self.data = initData
		self.left = None
		self.right = None

	def setData(self,newData):
		self.data = newData

	def getData(self):
		return self.data

	def setLeft(self, newNode):
		self.left = newNode

	def getLeft(self):
		return self.left

	def setRight(self, newNode):
		self.right = newNode

	def getRight(self):
		return self.right

class BinaryTree:
	def __init__(self, initData):
		self.root = Node(initData)

	def insertLeft(self, initData):
		temp = Node(initData) if self.root.getLeft() == None: self.root.setLeft(temp) else: temp.setLeft = self.root.getLeft() def insertRight(self, initData):
		temp = Node(initData)
		if self.root.getRight() == None:
			self.root.setRight(temp)
		else:
			self.root.setRight(temp.setRight(root.getRight()))

	def getRightChild(self):
		return self.root.getRight()

	def getLeftChild(self):
		return self.root.getLeft()

	def setRootVal(self, newRoot):
		self.node.setData = newRoot

	def getRootVal(self):
		return self.root.getData()


# r = BinaryTree('a')
# print(r.getRootVal())
# print(r.getLeftChild())
# r.insertLeft('b')
# print(r.getLeftChild())
# print(r.getLeftChild().getData())
# r.insertRight('c')
# print(r.getRightChild())
# print(r.getRightChild().getData())
# r.getRightChild().setData('hello')
# print(r.getRightChild().getData())