class Node:

  def __init__(self, data = None):
    self.data = data
    self.next = None

  
class LinkedList:

  def __init__(self,):
    self.head = None

  def insert_data(self, data):
    if(self.head):
      new_node = Node(data)
      new_node.next = self.head
      self.head = new_node
    else:
      new_node = Node(data)
      self.head = new_node
      new_node.next = None
  
  def display(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next

  def midlefinder(self):
    current = self.head
    midcheck = self.head
    while(current):
      current  = current.next.next
      mid_data  = midcheck.data
      midcheck = midcheck.next
    
    print("Mid_data: "mid_data)
      


llist = LinkedList()
llist.insert_data(10)
llist.insert_data(11)
llist.insert_data(12)
llist.insert_data(13)
llist.insert_data(14)
llist.insert_data(15)
llist.insert_data(16)
llist.insert_data(17)
llist.insert_data(18)
llist.insert_data(19)
llist.display()
llist.midlefinder()
