class Node:
  def __init__(self,data=None):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  
  def insert_data(self, data):
    new_node = Node(data)
    if(self.head):
      new_node.next = self.head
      self.head = new_node
    else:
      self.head = new_node
  
  def display(self):
    current = self.head
    if(current == None):
      print("List is empty")
      return 
    while(current):
      print(current.data, "->", end = ' ')
      current = current.next
    print("None", end = ' ')


# Naive Approach 
  # def Loopdetecter(self):
  #   current = self.head
  #   if(current == None):
  #     print("List is empty!")
  #     return
  #   s = set()
  #   while(current):
  #     if(current.data in s):
  #       print("Yup There is a Loop here!")
  #       return
  #     s.add(current.data)
  #     current = current.next
  #   print("I think there is no Loop in this!")

# Floyd's Approach
  def Loopdetecter(self):
    slower = self.head
    faster = self.head.next

    while(slower and faster and faster.next):
      if slower == faster:
        print("Yup there is a Loop here!")
        return
      slower = slower.next
      faster = faster.next.next
    print("Clear! There is no Loop here")
    
      
    # while(current):
llist = LinkedList()
llist.insert_data(10)
llist.insert_data(11)
llist.insert_data(12)
llist.insert_data(13)
#creating manual loop
# llist.head.next.next.next.next = llist.head
llist.Loopdetecter()
llist.display()
