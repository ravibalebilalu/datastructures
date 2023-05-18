class Node:
    def __init__(self,data = None):
        self.data = data
        self.prev = None
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("No Data")
        else:
            curent_node = self.head
            while curent_node:
                print(curent_node.data,"<==>",end = " ")
                curent_node = curent_node.next
    def front_load(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curent_node = self.head
            curent_node.prev = new_node
            new_node.next = curent_node
            self.head = new_node
    
    def back_load(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head  = new_node
        else:
            curent_node = self.head
            while curent_node.next:
                curent_node = curent_node.next
            curent_node.next = new_node
            new_node.prev = curent_node
    
    def insert_at(self,index,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        elif index == 0:
            self.front_load(data)
        else:
            curent_node = self.head
            count = 0
            while curent_node:
                if count == index - 1:
                    new_node.prev = curent_node
                    new_node.next = curent_node.next
                    curent_node.next = new_node
                count += 1
                curent_node = curent_node.next
    def front_remove(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head =  None
        else:
            curent_node = self.head
            self.head = curent_node.next
            curent_node.next = None
            self.head.prev = None

    def back_remove(self):
        if self.head is None:
            return
        else:
            previuos_node = self.head
            curent_node = self.head.next
            while curent_node.next:
                curent_node = curent_node.next
                previuos_node = previuos_node.next
            previuos_node.next = None
            curent_node.prev = None
    def remove_at(self,index):
        if self.head is None:
            return
        elif index == 0:
            self.front_remove()
        else:
            previuos_node = self.head
            curent_node = self.head.next
            count = 0
            while curent_node:
                if count == index - 1 :
                    previuos_node.next = curent_node.next
                    if curent_node.next:

                        curent_node.next.prev = previuos_node
                    curent_node.next = None
                    curent_node.prev = None
                curent_node = curent_node.next
                previuos_node = previuos_node.next
                count += 1



    
     






l = LinkedList()
g = [i for i in range(16,52,3)]
for i in g:
    l.back_load(i)
print("Our original doubly linked list : ")
l.display()

print("\n.........................\n")
print("Add 10 at starting :")

l.front_load(10)
l.display()

print("\n.........................\n")
print("Add 60 at ending :")
l.back_load(60)
l.display()

print("\n.........................\n")
print("Add 30 at position 6 :")
l.insert_at(6, 30)
l.display()

print("\n.........................\n")
print("remove first item :")
l.front_remove()
l.display()

print("\n.........................\n")
print("remove last item :")
l.back_remove()
l.display()

print("\n.........................\n")
print("Remove 5th eliment :")
l.remove_at(5)
l.display()
print("\n............THE END.............\n")
 