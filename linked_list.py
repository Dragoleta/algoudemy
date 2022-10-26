from cProfile import label


class Node:
    def __init__(self, label):
        self.label = label
        self.next =None

    def getLabel(self):
        return self.label

    def setLabel(self):
        self.label = label

    def getNext(self):
        return self.next
    
    def setNext (self, next):
        self.next =next

class LinkedLIst:
    def __init__(self):
        self.first = None
        self.last = None
        self.len_list = 0

    def push(self, label, index):
        if index >= 0:
            node = Node(label)
        if self.empty():
            self.first = node
            self.last = node
        else: 
            if index == 0:
                node.setNext(self.first)
                self.first = node
            elif index >= self.len_list:
                self.last.setNext(node)
                self.last=node
            else:
                prevNode = self.first
                currentNode = self.first.getNext()
                currentIndex= 1

                while currentNode != None:
                    if currentIndex == index:
                        node.setNext(currentNode)
                        prevNode.setNext(node)
                        break
                    prevNode = currentNode
                    currentNode = currentNode.getNext()
                    currentIndex +=1
        self.len_list += 1

    def pop(self, index):
        flagRemove = False
        if not self.empty() and index >=0 and index < self.len_list:
            if self.first.getNext() == None:
                self.first = None
                self.last= None
                flagRemove = True
            elif index == 0:
                self.first = self.first.getNext()
                flagRemove = True
            else: 
                prevNode = self.first
                currentNode = self.first.getNext()
                currentIndex = 1

                while currentNode != None:
                    if currentIndex == index:
                        prevNode.setNext(currentNode.getNext())
                        currentNode.setNext(None)
                        flagRemove = True                        
                        break
                    prevNode = currentNode
                    currentNode = currentNode.getNext()
                    currentIndex +=1

        if flagRemove:
            self.len_list -= 1


    def empty(self):
        if self.len_list == 0:
            return True
        return False

    def length(self):
        print( self.len_list)

    def show(self):
        currentNode = self.first

        while currentNode != None:
            print(currentNode.getLabel(), end =" ")
            currentNode = currentNode.getNext()
        print(" ")




lista = LinkedLIst()

lista.push("Jorge", 0)
lista.push("gaby", 1)
lista.push("Amora", 2)
lista.show()
lista.push("Selene", 2)
lista.push("Cleoprata", 4)
lista.show()
lista.pop(4)
lista.show()
lista.length()




