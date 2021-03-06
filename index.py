#Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).

def countdown(num):
    new_list = []
    for i in range(num,-1,-1):
        new_list.append(i)
    return new_list
print(countdown(5))
print(countdown(10))

# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.  Example: print_and_return([1,2]) should print 1 and return 2

test_list = [1,2]

def print_and_return(param_list):
    print(param_list[0])
    return param_list[1]

print(print_and_return(test_list))

#First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length. 
#Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

test_list = [1,2,3,4,5]
def first_plus_len(param_list):
    sum = param_list[0] + len(param_list)
    return sum
print(first_plus_len(test_list))

#Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values 
# from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. 
# If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

test_list = [5,2,3,2,1,4]
test_list_2 = [3]
def values_greater_than_second(param_list):
    new_list = []
    if len(param_list) > 2:
        for i in range(0,len(param_list),1):
            if param_list[i] > param_list[1]:
                new_list.append(param_list[i])
        return new_list
    else:
        return False
print(values_greater_than_second(test_list))
print(values_greater_than_second(test_list_2))


test_list = [5,2,3,2,1,4]
test_list_2 = []
def values_greater_than_second_2(param_list):
    new_list = []
    if len(param_list) > 2:
        second_value = param_list[1]
        for num in param_list:
            if num > second_value:
                new_list.append(num)
        print(len(new_list))
        return new_list
    else:
        return False

print(values_greater_than_second_2(test_list))
print(values_greater_than_second_2(test_list_2))


#This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function 
# should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def this_len_that_val(size, value):
    new_list = []
    for i in range(0,size):
        new_list.append(value)
    return new_list
print(this_len_that_val(4,7))
print(this_len_that_val(6,2))