import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

"""
Using original code, it takes 9.9 seconds to find duplicates
There are 64 duplicates total
runtime: O(n^2) ?

Navigate both names directories and make the runtime more efficient to find duplicates.
runtime = second

Can use one of the data structures we worked on in week's projects

CONSTRAINTS: cannot use list

input: both lists
output: duplicates only

Questions: 
1. Will we need to put both in binary search trees
2. Can  we separate the two loops?


PLAN: 
Use data structure from week's project that has best runtime: Binary search tree O(log n)
Import it
name_1
name_2

Pass in the names_1 into BST
loop through names_1 and insert into BST

Use contains to check names_2 against names_1

BST has values
roots
left and right

"""

duplicates = []
nameTree = BinarySearchTree(names_1.value)

for name in names_1:
    # insert each name into 
    nameTree.insert(name)
for name in names_2:
    # compare compare names_2 to BST to see if there ar duplicate
    # if returns true append to duplicate
    if nameTree.contains(name):
        duplicates.append(name)


# for name_1 in names_1:                #0(n)
#     for name_2 in names_2:            #0(n)
#         if name_1 == name_2:          #
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")



# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
