#implimentation of stack in LinkedList
class Node:
    def __init__(self,data = 0,next_node = None):
        self.data = data
        self.next_node = next_node
class Stack:
    def __init__(self):
        self.top = None

    def display(self):

        if self.top is None:
            return
        else:
            present_top = self.top
            while present_top:
                print(present_top.data,end = " ")
                present_top = present_top.next_node

    def push(self,data):
        new_top = Node(data)
        if self.top is None:
            self.top = new_top
        else:
            present_top = self.top
            new_top.next_node = present_top
            self.top = new_top
    def pop(self):
        if self.top is None:
            return
        else:
            present_top = self.top
            top_data = present_top.data
            self.top = present_top.next_node
        return top_data
    def peak(self):
        if self.top is None:
            return
        else:
            return self.top.data

    def is_empty(self):
        return self.top == None
             

box  =  Stack()
print("Is box empty : ")
print(box.is_empty())
 
print("push some items in box :")
box.push( "R")
box.push("python")
box.push( "c++")
box.push( "java")
box.push("data_science")
box.display()
print("\nTake top item from box :")
print(box.pop())
print("Now our box looks like :")
box.display()
print("\n let us check top item :")
print(box.peak())