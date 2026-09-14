class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
class LinkedList:
        def __init__(self):
            self.head = None
            self.prev = Node
            self.next = None
            

node1=Node(25)
node2=Node(30)
node3=Node(35)
node4=Node(40)

node1.next=node2
node2.prev=node1

node2.next=node3
node3.prev=node2

node3.next=node4
node4.prev=node3
head=node1
new_node=Node(68)
new_node.prev=node2.next
new_node.prev = node2
node2.next.prev = new_node
node2.next = new_node

current=head

while current is not None:
    print(current.data,end="->")
    current=current.next #move next node 
print("None")
