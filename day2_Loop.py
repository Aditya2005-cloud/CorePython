# loop

value= True
# while value== True:
#     print("This is a while loop")
# # This is an infinite loop because the condition value==True will always be true. The loop will continue to execute indefinitely, printing "This is a while loop" repeatedly until the program is manually stopped or interrupted.

while value== True:
    print("This is a while loop")
    value= False
# This loop will execute only once because after the first iteration, the condition value==True will become false (since value is set to False), and the loop will terminate. It will print "This is a while loop" only one time.

while value:
    print("This is a while loop")
    value= False # or we can use break statement to exit the loop
# This loop will also execute only once for the same reason as the previous example. The condition value is evaluated as a boolean, and since value is initially True, the loop will run. After the first iteration, value is set to False, causing the loop to terminate. It will print "This is a while loop" only one time.

number= 0
while number<7:
    print(number)
    number+=1
# This loop will print the numbers from 0 to 6. The loop starts with number initialized to 0, and it continues to execute as long as number is less than 7. In each iteration, it prints the current value of number and then increments number by 1. Once number reaches 7, the condition number<7 becomes false, and the loop terminates.

item= ["apple", "banana", "cherry"]
for fruit in item:
    print(fruit)
# This loop will iterate over each element in the list item, which contains the strings "apple", "banana", and "cherry". In each iteration, the variable fruit takes on the value of the current element in the list, and it is printed. The output will be:
# apple
# banana
# cherry

for fruit in range(len(item)):
    print(item[fruit])
# This loop will achieve the same result as the previous loop, but it uses a different approach. The range(len(item)) generates a sequence of indices from 0 to the length of the list item minus one (0, 1, 2). In each iteration, the variable fruit takes on the value of the current index, and item[fruit] retrieves the corresponding element from the list. The output will be:
# apple 
# banana
# cherry


for i in range(5):
    print(i)
# This loop will print the numbers from 0 to 4. The range(5) function generates a sequence of numbers starting from 0 up to, but not including, 5. In each iteration, the variable i takes on the value of the current number in the sequence, and it is printed. The output will be:


for i in range(1, 6):
    if i == 3:
        continue
    print(i)
# This loop will print the numbers from 1 to 5, except for the number 3. The range(1, 6) function generates a sequence of numbers starting from 1 up to, but not including, 6. In each iteration, the variable i takes on the value of the current number in the sequence. If i is equal to 3, the continue statement is executed, which skips the rest of the loop body for that iteration and moves on to the next iteration. As a result, the output will be:


for i in range(1, 6):
    if i == 3:
        break
    print(i)
# This loop will print the numbers from 1 to 5, but it will stop executing once it reaches the number 3. The range(1, 6) function generates a sequence of numbers starting from 1 up to, but not including, 6. In each iteration, the variable i takes on the value of the current number in the sequence. If i is equal to 3, the break statement is executed, which immediately terminates the loop. As a result, the output will be:

for index , i in enumerate(item):
    print(index, i)