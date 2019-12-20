class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def __repr__(self):
    return f"value:{self.value} next_node: {self.next_node}"

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def __repr__(self):
    return f"Head= {self.head}"

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  """
  input: called upon the list itself
  1 --> 2 --> 3 --> 4 --> null
  
  output: list in reverse
  4 --> 3 --> 2 --> 1 --> null: technically we are changing the pointers direction

  Constraints:
  1. Can't have a tail

  We have a head == 0

  """

  def reverse_list(self):
    # initialize:
    # prev to None:
    prev = None
    # set current = self.head to keep track of where we are
    current = self.head
    # print("Whats the head",current)
    # while current !=None:
    while current is not None:
    # swaping by reference
      next_node = current.next_node
      prev = current
      current = next_node
    self.head = prev
    # need to print the rest
    print("after while",self.head)
    

new_list = LinkedList()
# print(new_list.add_to_head(2))
# print(new_list)
print(new_list.add_to_head(5))
print(new_list.add_to_head(7))
print(new_list.add_to_head(0))
print(new_list.add_to_head(3))
print(new_list)

print("Reverse",new_list.reverse_list())
print("after reverse",new_list)