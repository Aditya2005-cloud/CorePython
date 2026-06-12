#filter()filter(function, iterable)
# Read it as:
# Check every item.
# Keep it if the function says True.
# Remove it if the function says False.
def even(n):
    return n%2==0
num=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(even,num)))

def odd(x):
    return x%2!=0
print(list(filter(odd,num)))