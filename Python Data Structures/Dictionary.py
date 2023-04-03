# Python program to demonstrate working of dictionary clear()
text = {1: "geeks", 2: "for"}
text.clear()
print('text =', text)

original = {1: 'geeks', 2: 'for'}
new = original.copy()
new.clear()
print('new: ', new)
print('original: ', original)

d = {'coding': 'good', 'thinking': 'better'}
print(d.get('coding'))

# Python program to show working of items() method in Dictionary
# Dictionary with three items
Dictionary1 = { 'A': 'Geeks', 'B': 4, 'C': 'Geeks' }
print("Dictionary items:")
# Printing all the items of the Dictionary
print(Dictionary1.items())

# Dictionary with three keys
Dictionary1 = {'A': 'Geeks', 'B': 'For', 'C': 'Geeks'}
# Printing keys of dictionary
print(Dictionary1.keys())

seq = ('a', 'b', 'c')
print(dict.fromkeys(seq, None))

# Python 3 code to demonstrate working of pop()
# initializing dictionary
test_dict = {"Nikhil": 7, "Akshat": 1, "Akash": 2}
# Printing initial dict
print("The dictionary before deletion : " + str(test_dict))
# using pop to return and remove key-value pair.
pop_ele = test_dict.pop('Akash')
# Printing the value associated to popped key
print("Value associated to popped key is : " + str(pop_ele))
# Printing dictionary after deletion
print("Dictionary after deletion is : " + str(test_dict))

d = {1: '001', 2: '010', 3: '011'}
print(d.popitem())

d = {'a': 97, 'b': 98, 'c': 99, 'd': 100}
# space key added using setdefault() method
d.setdefault(' ', 32)
print(d)

# Python program to show working of update() method in Dictionary
# Dictionary with three items
Dictionary1 = {'A': 'Geeks', 'B': 'For', }
Dictionary2 = {'B': 'Geeks'}
# Dictionary before Updation
print("Original Dictionary:")
print(Dictionary1)
# update the value of key 'B'
Dictionary1.update(Dictionary2)
print("Dictionary after updation:")
print(Dictionary1)

dictionary = {"raj": 2, "striver": 3, "vikram": 4}
print(dictionary.values())  