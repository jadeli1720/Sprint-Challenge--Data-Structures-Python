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
1. append(): --> 

['a', 'b', 'c', 'd']
['a', 'b', 'c', 'd', 'e']
['f', 'b', 'c', 'd', 'e']
['f', 'g', 'h', 'i', 'e']
['k', 'g', 'h', 'i', 'j']

2. get()

"""


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity          # limit
        self.current = None
        self.storage = DoublyLinkedList() 

    def __repr__(self):
        return f" Capacity: {self.capacity}, Current: {self.current}, Storage:{self.storage}"

    def append(self, item):
        # if self.capacity >= self.storage.length
        if  self.storage.length >= self.capacity:
            # remove from tail
            self.storage.remove_from_tail()
            # then add to head
            self.storage.add_to_head(item)
            # current += 1
            # print(current)
        # else add to head
        self.storage.add_to_head(item)
        # current += 1


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = [] 

        # current = head
        current = self.storage.head
        # while current = head
        while current: # we need to grab ALL items in []
            list_buffer_contents.append(current.value)
            current = current.next
        
        print(list_buffer_contents)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass


buffer = RingBuffer(5)

print(buffer.append('a'))
print(buffer.append('b'))
print(buffer.append('c'))
print(buffer.append('d'))
print(buffer.append('e'))
print(buffer.get())