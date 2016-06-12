#Tree implementation of 
def BinaryTree(r):
	return [r, [], []]

def insertLeft(root, newBranch):
	t = root.pop(1)
	newNode = [newBranch, [],[]]
	if len(t) > 0:
		newNode[1] = t
		root.insert(1, newNode)
	else:
		root.insert(1,newNode)
		
	return root

def insertRight(root, newBranch):
	t = root.pop(2)
	newNode = [newBranch,[],[]]
	if len(t) > 0:
		newNode[2] = t
		root.insert(2,newNode)
	else:
		root.insert(2,newNode)
	return root

def getRootVal(root):
	return root[0]

def setRootVal(root, newVal):
	root[0] = newVal

def getLeftChild(root):
	return root[1]

def getRightChild(root):
	return root[2]


def buildTree():
	a = BinaryTree('a')
	insertLeft(a, 'b')
	insertRight(getLeftChild(a),'d')
	insertRight(a,'c')
	insertLeft(getRightChild(a),'e')
	insertRight(getRightChild(a),'f')

	return a

print(buildTree())
