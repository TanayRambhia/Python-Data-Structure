# set of letters
s = {'g', 'e', 'k', 's'}

# adding 's'
s.add('f')
print('Set after updating:', s)

# Discarding element from the set
s.discard('g')
print('\nSet after updating:', s)

# Removing element from the set
s.remove('e')
print('\nSet after updating:', s)

# Popping elements from the set
print('\nPopped element', s.pop())
print('Set after updating:', s)

s.clear()
print('\nSet after updating:', s)

# Python3 program to demonstrate the use
# of join() function
set1 = {1, 2, 3, 4}
# function to copy the set
set2 = set1.copy()
# prints the copied set
print(set2)	

# Python code to get the difference between two sets
# using difference() between set A and set B

# Driver Code
A = {10, 20, 30, 40, 80}
B = {100, 30, 80, 40, 60}
print (A.difference(B))
print (B.difference(A))

# Python code to get the difference between two sets
# using difference_update() between set A and set B
A = {10, 20, 30, 40, 80}
B = {100, 30, 80, 40, 60}
# Modifies A and returns None
A.difference_update(B)
# Prints the modified set
print (A)

s1 = {1, 2, 3}
s2 = {2, 3}
print(s1.intersection(s2))

A = {10, 20, 30, 40, 80}
B = {100, 30, 80, 40, 60}
# Modifies A and returns None
A.intersection_update(B)
print(A)

s1 = {1, 2, 3}
s2 = {4, 5, 6}
print(s1.isdisjoint(s2))

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5}
# Output True, since, s2 elements in s1
print(s2.issubset(s1))

A = {4, 1, 3, 5}
B = {6, 0, 4, 1, 5, 0, 3, 5}
print("A.issuperset(B) : ", A.issuperset(B))
print("B.issuperset(A) : ", B.issuperset(A))

s1 = {9, 1, 0}
s1.pop()
print(s1)

# Python program to demonstrate the use of symmetric_difference() method
list1 = [1, 2, 3]
list2 = [2, 3, 4]
list3 = [3, 4, 5]
# Convert list to sets
set1 = set(list1)
set2 = set(list2)
# Prints the symmetric difference when set is passed as a parameter
print(set1.symmetric_difference(set2))
# Prints the symmetric difference when list is passed as a parameter by converting it to a set
print(set2.symmetric_difference(list3))

# Python code to demonstrate working of symmetric_difference_update()

A = {'p', 'a', 'w', 'a', 'n'}
B = {'r', 'a', 'o', 'n', 'e'}
# result is always none.
result = A.symmetric_difference_update(B)
print('A = ', A)
print('B = ', B)
print('result = ', result)

A = {2, 4, 5, 6}
B = {4, 6, 7, 8}
print("A U B:", A.union(B))

# Python program to demonstrate the use of update() method
list2 = [1, 4, 2, 3, 5]
alphabet_set = {'a', 'b', 'c'}
# lists converted to sets
set1 = set(list2)
# Print the updated set
print(set1)
set1.update(alphabet_set)
print(set1)
