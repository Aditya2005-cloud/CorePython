#Using reduce(it takes many values and combines them into one final value.)
from functools import reduce
def add(a,b):
    return a+b
a=[1,2,3,4,5,6,7,8,9]
print(reduce(add,a))


# map() → transform every item.
# filter() → keep selected items.
# reduce() → combine all items into one result.