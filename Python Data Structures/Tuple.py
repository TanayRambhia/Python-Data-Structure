# Creating tuples
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
# count the appearance of 3
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)

# Creating tuples
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
# getting the index of 3
res = Tuple.index(3)
print('First occurrence of 3 is', res)
# getting the index of 3 after 4th
# index
res = Tuple.index(3, 4)
print('First occurrence of 3 after 4th index is:', res)

languages = ('C', 'JAVA', 'C++','VB','Python','PHP')
print(max(languages))
print(min(languages))

var=sorted(languages)
print(var)
nt=(1,2,3,4,5)
print(sum(nt))
print(any((1,))) # returns true if any element exists