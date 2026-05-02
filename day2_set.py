# set practice

my_set={1,2,3,4,5}
print(my_set) # Output: {1, 2, 3, 4, 5} sets are unordered and do not allow duplicates
my_set.add(6) # Adding an element to the set
print(my_set) # Output: {1, 2, 3, 4, 5, 6}
my_set.add(3) # Adding a duplicate element, it will not be added
print(my_set) # Output: {1, 2, 3, 4, 5, 6} no change as 3 is already in the set
my_set.remove(2) # Removing an element from the set
print(my_set) # Output: {1, 3, 4, 5, 6}
my_set.discard(10) # Discarding an element that does not exist, no error will be raised
print(my_set) # Output: {1, 3, 4, 5, 6}
my_set.clear() # Clearing all elements from the set 
print(my_set) # Output: set() an empty set  


name_set={"Alice", "Bob", "Charlie"}
name_set2={"David", "Eve", "Frank", "Alice"}
Sub_names=name_set - name_set2 # Set difference, names in name_set but not in name_set2
print(Sub_names) # Output: {'Bob', 'Charlie'} Alice is in both sets, so it is not included in the result

added_names=name_set | name_set2 # Set union, all unique names from both sets we can use + or | operator for union
print(added_names) # Output: {'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'} all unique names from both sets  
common_names=name_set & name_set2 # Set intersection, names that are in both sets
print(common_names) # Output: {'Alice'} only Alice is common in both sets
