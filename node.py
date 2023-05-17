class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

    def add_nodes(self,num):
        new_node = Node(num)
        if self.data is None:
            self.data = new_node
        else:
            curent_data = self.data
            while curent_data.next:
                curent_data = curent_data.next
            curent_data.next = new_node

    def display(self):
        if self.data is None:
            print("empty")
        else:
            curent_data = self.data
            while curent_data:
                print(curent_data.data,end = " ")
                curent_data = curent_data.next


c = Node()
c.add_nodes(18)
c.add_nodes( 36)
c.add_nodes( 87)
c.add_nodes("shreekrishna")
c.add_nodes("python")
c.display()