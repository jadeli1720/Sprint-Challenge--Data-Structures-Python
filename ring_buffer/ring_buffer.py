from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import Stack
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

['a', 'b', 'c']
['d', 'b', 'c']
['e', 'b', 'c']


replacing by passing through reference?

2. get()

"""


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity          # limit
        self.current = None
        self.storage = DoublyLinkedList() #will hold all of the items

    def __repr__(self):
        return f"storage: {self.storage}"

    # def __str__(self):
    #     return f"current: {self.current}"

    def append(self, item):
        current_item = item
        print("current item:", current_item)
        # use current as a pointer!!!

        # if self.storage.length < self.capacity:
        #     self.storage.add_to_head(current_item)
        #     #after append, move storage to follow the tail
        #     self.current = self.storage.tail # there will always be a none value at the end. This gives us access to current.next!!!!!
        #     print("current", self.current)
            
        if self.storage.length == self.capacity:           # This is limit 
            if self.current == self.storage.tail:          # If current is == to the tail
                self.storage.remove_from_tail()            # Remove from the tail which is the oldest
                self.storage.add_to_tail(current_item)     # add new item to the tail
                self.current = self.storage.head           # make current the head
                print("nested if current", self.current)   #[e]
                
            else:                                               # length > capacity
                # print('current b4 else happens', self.storage.head)     
                self.current.insert_after(current_item)         #insert item after current 
                self.storage.length += 1                        # go through the length             
                print("prev  current", self.current.prev)
                print("current", self.current)
                print("current next", self.current.next)
                self.current = self.current.next               #make current equal next                       
                print("nested 1 else current", self.current.next)
                self.storage.delete(self.current.next)         #back up by one 
                print("nested 2 else current", self.current.next)      

            # print("Head", self.storage.head) #--> c
            # print("Tail", self.storage.tail) # --> a
                # # print("nested else current", self.current)
        
        else:
            # add to head
            self.storage.add_to_head(current_item)
            #after append, move storage to follow the tail
            self.current = self.storage.tail # there will always be a none value at the end. This gives us access to current.next!!!!!
            print("current", self.current)

        print("Head", self.storage.head) #--> c
        print("Tail", self.storage.tail) # --> a

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = [] 
        # current = tail --> print in direction expected in test
        current = self.storage.tail
        
        # while current
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


buffer = RingBuffer(5)
print(buffer.get())
print(buffer.append('a'))
print(buffer.append('b'))
print(buffer.append('c'))
print(buffer.append('d'))
print(buffer.append('e'))
print(buffer.append('f'))
print(buffer.append('g'))
print(buffer.get())