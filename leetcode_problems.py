# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
def sum_of_two(num,target):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i]+num[j]==target:
                return [i,j]
target=int(input("enter the target no: "))
nums=[2,3,4,5,6,78,9,1,22,45,78,99,0]
print(sum_of_two(nums,target))


numbers = [i for i in range(1, 6)]
print(numbers)
evens = [i for i in range(1, 11) if i % 2 == 0]
print(evens)