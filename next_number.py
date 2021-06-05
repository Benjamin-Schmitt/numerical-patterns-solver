# pattern solver
# e.g. Which number comes next in this row:
# 2 4 6 8 _

# Here the answer is obv. 10, because we're incrementing each number by 2

# How would an algorithm look like that solves this problem?
# 1. Find the difference between each number in the row
# 2. Look for a pattern by finding the difference between 2 or 3 numbers (when fibonacci)
# 3. Then look for the difference between the difference. That is the key


#imports
import math


#1.  create a sequence of numbers, store it in a list variable
numbers = []
for element in range(4):
    numbers.append(int(input('give me a number: \n >>> ')))
print(f'the input row is: {numbers}')

#2. Check list for differences between the numbers to find the hidden function
difference = []
difference.append(numbers[1]-numbers[0])
difference.append(numbers[2]-numbers[1])
difference.append(numbers[3]-numbers[2])
print(f'second row is:      {difference}')

###############
## Patterns: ##
###############
#1. check for difference of difference to find square root patterns
difference_difference = []
difference_difference.append(difference[1]-difference[0])
difference_difference.append(difference[2]-difference[1])
same_diff = difference_difference[0] == difference_difference[1]
print(f'the third row is:     {difference_difference}')


# multiplication patterns ##########################
#check for multiplication pattern in the input row
for i in range(100):
    if numbers[0] * i == numbers[1] and numbers[1] * i == numbers[2] and numbers[2] * i == numbers[3]:
        print('could be a multiplication pattern')
        print('next number is:')
        print(numbers[3] * i)

# check for multiplication pattern in the second row
for i in range(100):
    if difference[0] * i == difference[1] and difference[1] * i == difference[2]:
        print(f'multiplication pattern in the second row detected. The first number in the second row, multiplied by {i} gives the second number in the second row. We multiply the last number in the second row {difference[2]} with {i} and add this to the last number in the input row. Therefore the next number is: ')
        print(f'\n >>> difference[2] * i + numbers[3]')



# addition patterns ##################################
if difference[0] == difference[1] == difference[2]:
    print('\n \n the difference in the first row is always the same number. This indicates a simple addition or subtraction function')
    print(f"Therefore, we're adding this difference. The next number is: \n >>> {difference[0] + numbers[3]}")


# square root patterns ##################################
elif same_diff == True:
    print('a second row pattern with the same number indicates a square root pattern')
    print((math.sqrt(numbers[3])+1)*(math.sqrt(numbers[3])+1))










