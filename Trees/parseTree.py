import treeNode


class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):

        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        return False
    
    def size(self):
        return len(self.items)


def buildParseTree(expr):

	exprList = expr.split()

	parseTree = treeNode.BinaryTree(None)
	currentNode = parseTree.root
	parentStack = Stack()
	#parentStack.push(currentNode)

	for token in exprList:
		if token == '(':
			currentNode.setLeft(treeNode.Node(None))
			#Push parent into stack when we descend
			parentStack.push(currentNode)
			#Set currentNode to left Child
			currentNode = currentNode.getLeft()
		elif token in ['+','-','/','*']:
			currentNode.setData(token)
			currentNode.setRight(treeNode.Node(None))
			parentStack.push(currentNode)
			currentNode = currentNode.getRight()	
		elif token.isdigit():
			currentNode.setData(token)
			currentNode = parentStack.pop()
		elif token == ')':
			if not parentStack.isEmpty():
				currentNode = parentStack.pop()
	return parseTree

pt = buildParseTree("( 3 + ( 4 * 5 ) )")
print(pt.getRootVal())
print(pt.getLeftChild().getData())
print(pt.getRightChild().getData())
print(pt.getRightChild().getLeft().getData())
print(pt.getRightChild().getRight().getData())