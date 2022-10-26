from cProfile import label
from turtle import left, right


class Node:
    def __init__(self, label):
        self.label = label
        self.left= None
        self.right= None

    def getLabel(self):
        return self.label
    def getRight(self):
        return self.right
    def getLeft(self):
        return self.left

    def setLabel(self, label):
        self.label = label
    def setRigth(self, right):
        self.right = right
    def setLeft(self, left):
        self. left = left

class BinaryTree:
    def __init__(self) -> None:
        self.root = None
    
    def getRoot(self):
        return self.root

    def insert(self, label):
        node = Node(label)

        if self.isEmpty():
            self.root  = node
        else:
            parentNode = None
            currentNode = self.root
           
            while True:
                if currentNode != None:
                    parentNode = currentNode
                    if node.getLabel() < currentNode.getLabel():
                        currentNode = currentNode.getLeft()
                    else:
                        currentNode = currentNode.getRight()
                else:
                    if node.getLabel() < parentNode.getLabel():
                        parentNode.setLeft(node)
                    else:
                        parentNode.setRigth(node)
                    break

    def isEmpty(self):
        if self.root ==None:
            return True
        return False

    def show(self, currentNode):
        if currentNode != None:
            print(currentNode.getLabel(), end=" ")
            self.show(currentNode.getLeft())
            self.show(currentNode.getRight())

    def removeNode(self, label):
        parrentNode = None
        currentNode = self.root

        while currentNode != None:
            if label == currentNode.getlabel():
                # if node has no children
                if currentNode.getLeft() ==None and currentNode.getRight() == None:
                    if parrentNode ==None:
                        self.root=None
                    else:
                        if parrentNode.getLeft() == currentNode:
                            parrentNode.setLeft(None)
                        else:
                            parrentNode.setRight(None)
                # if node has one children
                elif currentNode.getLeft() ==None or currentNode.getRight ==None:
                    if parrentNode == None:
                        if currentNode.getLeft() != None:
                            self.root = currentNode.getLeft()
                        else:
                            self.root = currentNode.getRight()
                    else:
                        if currentNode.getLeft != None:
                            if parrentNode.getLeft() == currentNode:
                                parrentNode.setLeft(currentNode.getLeft())
                            else:
                                parrentNode.setRight(currentNode.getLeft())
                        else: 
                            if parrentNode.getLeft() == currentNode:
                                parrentNode.setLeft(currentNode.getRight())
                            else:
                                parrentNode.setRight(currentNode.getRight())
                # if node has two childern
                elif currentNode.getLeft != None and currentNode.getRight() !=None:
                    smallerNodeParrent = currentNode
                    smallerNode = currentNode.getRight()
                    nextSmallerNode = currentNode.getRight().getLeft()
                    while nextSmallerNode != None:
                        smallerNodeParrent = smallerNode
                        smallerNode = nextSmallerNode
                        nextSmallerNode = smallerNode.getLeft()
                    
                    if parrentNode==None:
                        if self.root.getRight().getLabel() == smallerNode.getLabel():
                            smallerNode.setLeft(self.root.getLfet())
                        else:
                            if smallerNodeParrent.getlet().getLabel() == smallerNode.getLabel():
                                smallerNodeParrent.setLeft(None)
                            else:
                                smallerNodeParrent.setRight(None)
                            smallerNode.setLeft(currentNode.getLeft())
                            smallerNode.setRight(currentNode.getRight())
                        self.root=smallerNode





t = BinaryTree()

t.insert(3)
t.insert(5)
t.insert(4)
t.insert(3)
t.insert(7)
t.insert(6)
t.insert(10)
t.insert(20)
t.insert(15)
t.insert(32)
t.insert(64)
t.show(t.getRoot())

