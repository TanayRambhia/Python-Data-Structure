# Adds List Element as value of List.
list1 = ['Mathematics', 'chemistry', 1997, 2000]
list1.append(20544)
print(list1)

list2 = ['Mathematics', 'chemistry', 1997, 2000]
# Insert at index 2 value 10087
list2.insert(2, 10087)
print(list2)


List1 = [1, 2, 3]
List2 = [2, 3, 4, 5]
 
# Add List2 to List1
List1.extend(List2)
print(List1) 
# Add List1 to List2 now
List2.extend(List1)
print(List2)

List3 = [6, 7, 8]
List4 = [13, 31, 14, 51]
 
# Add List2 to List1
List3.append(List4)
print(List3) 
# Add List1 to List2 now
List4.append(List3)
print(List4)

List = [1, 2, 3, 4, 5]
print(sum(List))

List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.count(1))

List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(len(List))

List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.index(2))

List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.index(2, 2))

numbers = [5, 2, 8, 1, 9]
print(min(numbers))

numbers = [5, 2, 8, 1, 9]
print(max(numbers))


List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
#Reverse flag is set True
List.sort(reverse=True)
#List.sort().reverse(), reverses the sorted list
print(List)	

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print(List.pop())
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
print(List.pop(0))

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
del List[0]
print(List)

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5]
List.remove(3)
print(List)

