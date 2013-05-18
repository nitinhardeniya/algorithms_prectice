

class Node(object):
    """a single Node of Linkedlist"""
    def __init__(self, data=None,next_node=None):
        super(Node, self).__init__()
        self.data = data
        self.next=next_node

    def GetNextNode(self):
        return self.next

    def SetNextNode(self,next_node):
        self.next=next_node

    def Getdata(self):
        return self.data

    def SetData(self,mydata):
        self.data=mydata

class Linkedlist(object):
    """docstring for Linkedlist"""
    def __init__(self):
        self.root=Node()
        self.root.SetNextNode(self.root)
        self.length=0

    def getRootNode(self):
        return self.root

    def Inseart(self,data):
        newNode=Node()
        newNode.SetData(data)
        newNode.SetNextNode(self.root.GetNextNode())
        self.root.SetNextNode(newNode)
        self.length = self.length + 1

    def GetLength(self):
        return self.length

    def Traverse(self):
        tnode = self.root.GetNextNode()
        while tnode != self.root:
            print str(tnode.Getdata()) + "-->",
            tnode = tnode.GetNextNode()



if __name__ == "__main__":

    intlist = Linkedlist()
    for x in range(10):
        intlist.Inseart(x + 1)
    print "There are %d elements in the list" % intlist.GetLength()
    intlist.Traverse()


        