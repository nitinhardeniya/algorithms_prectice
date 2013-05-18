

class node:
    def __init__(self):
        self.data = None 
        self.next = None 


class linked_list:
    def __init__(self):
        self.cur_node = None

    def add_node(self, data):
        new_node = node() 
        new_node.data = data
        new_node.next = self.cur_node 
        self.cur_node = new_node 

    def list_print(self):
        node = self.cur_node 
        while node:
            print node.data,
            print '-->'
            node = node.next

    def delete_node(self,delkey):
        """ To-modify"""
        node=self.cur_node
        while node.next.next.data!=delkey:
            node=node.next
        return 

    def get_k(self,k):

        node=self.cur_node
        #print node.data
        for i in range(k):
            node=node.next


        return node.data

    def Find(self,key):
        node=self.cur_node
        while node:
            if node.data==key:
                return True
            node=node.next
        return False



ll = linked_list()
ll.add_node(1)
ll.add_node(2)
ll.add_node(3)
ll.add_node(4)
ll.add_node(5)
ll.add_node(6)
ll.add_node(7)
ll.list_print()
print ll.get_k(5)
print ll.Find(4)
print ll.Find(0)
