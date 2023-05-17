#implimentation of Queue using singly linked list
class Node:
    def __init__(self,data = 0,next = None):
        self.data = data
        self.next = next
class Queue:
    def __init__(self):
        self.head = None
    
    def display(self):
        if self.head is None:
            return
        else:
            curent_node = self.head
            while curent_node:
                print(curent_node.data,end = " ")
                curent_node = curent_node.next

    
    def enqueue(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curent_node = self.head
            while curent_node.next:
                curent_node = curent_node.next
            curent_node.next = new_node
    


    def dequeue(self):
        if self.head is None:
            return
        else:
            curent_node = self.head
            first_data = curent_node.data
            self.head = curent_node.next
        return first_data

    def is_empty(self):
        return self.head == None
    def size(self):
        count = 0
        curent_node = self.head
        while curent_node:
            curent_node = curent_node.next
            count += 1
        return count
        
data = Queue()
print("enqueue results :")
data.enqueue(24)
data.enqueue(48)
data.enqueue("java")
data.enqueue("python")
data.enqueue("mojo")
data.display()
print("###############")
print("dequeue result :")
data.dequeue()
data.display()


         
