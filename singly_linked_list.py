#implementtion of Linkedlist

class Node:
    def __init__(self,data = 0,next = None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("empty")
        else:
            curent_node = self.head
            while curent_node:
                print(curent_node.data,"-->",end = " ")
                curent_node = curent_node.next

    def front_load(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curent_node = self.head
            new_node.next = curent_node
            self.head = new_node
         
    def back_load(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curent_node = self.head
            while curent_node.next:
                curent_node = curent_node.next
            curent_node.next = new_node
    
    def load_at(self,index,data):
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
                    new_node.next = curent_node.next
                    curent_node.next = new_node
                count += 1
                curent_node = curent_node.next
    def remove_at_front(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head = None
        else:
            curent_node = self.head.next
            
            self.head = curent_node

    def remove_at_back(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head = None
        else:
            previous_node = self.head
            curent_node = self.head.next
            while curent_node.next:
                curent_node = curent_node.next
                previous_node = previous_node.next
            previous_node.next = None

    def remove_at(self,index):
        if self.head is None:
            return
        elif index == 0:
            self.remove_at_front()
        else:
            previous_node = self.head
            curent_node = self.head.next
            count = 0
            while curent_node:
                if count == index - 1:
                    previous_node.next = curent_node.next
                    curent_node.next = None
                curent_node = curent_node.next
                previous_node = previous_node.next
                count += 1
    def size(self):
        curent_node = self.head
        count = 0
        while curent_node:
            curent_node = curent_node.next
            count += 1
        return count
    def is_empty(self):
        return self.head == None
#####################
def series(start,end,intervel):
    result = []
    i = start
    while i <= end:
        result.append(i)
        i += intervel
    return result
   ######################
 
mylist = LinkedList()

nums = series(560,580,2)

for i in nums:
    mylist.back_load(i)
    
mylist.display()

print("\n size of mylist :",mylist.size())

print("\n insert 550 at front : \n")
mylist.front_load(550)
mylist.display()
print("\n insert 590 at back : \n")
mylist.back_load(590)

mylist.display()





 