class Node:
   def __init__(self,data):
    self.data=data
    self.next=None
    self.prev=None
class CircularDoublyLinkedList:
  def __init__(self):
    self.head=None
  def insert_at_end(self,data):
    new_node=Node(data) 
    if not self.head:
        self.head=new_node
        new_node.next=new_node
        new_node.prev=new_node
        return
    temp=self.head.prev
    temp.next=new_node
    new_node.prev=temp
    new_node.next=self.head
    self.head.prev=new_node
  def display(self):
    if not self.head:
      return
    temp=self.head
    while True:
      print(temp.data,end=",<->")
      temp=temp.next
      if temp==self.head:
        break
      print("(Back to Head)")
#usage
cdll=CircularDoublyLinkedList()
cdll.insert_at_end(10) 
cdll.insert_at_end(20)
cdll.insert_at_end(30)
cdll.display()