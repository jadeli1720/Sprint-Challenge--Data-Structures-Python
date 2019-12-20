from doubly_linked_list import DoublyLinkedList
# from ring_buffer.doubly_linked_list import Stack
# from ring_buffer.doubly_linked_list import Queue

"""
UNDERSTANDING: --> Similar to LRU_cache
1. Fixed Size
2. When full, new element is inserted (head), oldest element is overwritten (tail)
3. 2 methods get() and appends()
    a. appends(): adds elements to buffer
    b. get(): RETURNS all of the elements in the buffer in a list given ==> list_buffer_contents
4. It should NOT RETURN NONE VALUES in the list even if they are present in the ring buffer
5. May NOT use a Python List in implementing the append method

QUESTIONS:
1. How is this and LRU cache similar different?
2. Can we utilize stack and queue data structures to solve the problem
3. What is the test file looking for?

input: item
output:

PLAN: 
1. append(): --> adding to tail each time which is the newest items

['a', 'b', 'c', 'd']
['a', 'b', 'c', 'd', 'e']
['f', 'b', 'c', 'd', 'e']
['f', 'g', 'h', 'i', 'e']
['k', 'g', 'h', 'i', 'j']

stack

replacing by passing through reference?

2. get()

"""


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity          # limit
        self.current = None
        self.storage = DoublyLinkedList() #will hold all of the items

    # def __repr__(self):
    #     return f"current: {self.storage.head}"

    # def __str__(self):
    #     return f"current: {self.current}"

    def append(self, item):
        current_item = item
        print("current item:", current_item)
        print("capacity", self.capacity)
        # if self.capacity > self.storage.length --> if the value turn into a NoneType, check your operator
        if self.storage.length < self.capacity:
            # add to head
            self.storage.add_to_head(current_item)
            
        if  self.storage.length > self.capacity: # This needs to limit
            
            # add to 
            self.storage.add_to_tail(current_item)
            # self.current = self.storage.tail 
            print("current item:", self.current)
            print("head", self.head)

        



    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = [] 
        # current = tail --> print in direction expected in test
        current = self.storage.tail
        print(self.storage.head)
        # while current = head
        while current: # we need to grab ALL items in []  iteration
            list_buffer_contents.append(current.value)
            current = current.prev

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass


buffer = RingBuffer(3)
print(buffer.get())
print(buffer.append('a'))
print(buffer.append('b'))
print(buffer.append('c'))
# print(buffer.get())
print(buffer.append('d'))
print(buffer.get())
# print(buffer.append('e'))
# print(buffer.get())