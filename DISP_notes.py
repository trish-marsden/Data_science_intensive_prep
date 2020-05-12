# def mult_x_and_y():
#     # get some input from a user
#     x = input('Input a value for x: ')

#     print(f'{x} is of type {type(x)}')


#     # convert that value to an int
#     print('\nconverting x')

#     x = int(x)
#     print(f'{x} is now of type {type(x)}')

#     # take in a second value and multiply the two
#     y = input('\nInput a value for y: ')
#     y = int(y)
#     print(f'{x} * {y} = {x*y}')

# mult_x_and_y()

'''
ctrl + c + k allows you to comment out a block of code at once
'''
# def multiply_by_three(x):
#     x *= 3
#     x = float(x)
#     return x
# print(multiply_by_three(3))


# def is_difference_truthy(x,y):
#     truthy = bool(x - y)
#     return truthy
# print(is_difference_truthy(6, 7))

# def create_three_digit_num(n, m, p):
#     p = str(p)
#     m = str(m)
#     n = str(n)
#     number = int(p + m + n)
#     return number
# print(create_three_digit_num(4, 5, 6))

# def create_three_digit_num(n, m, p):
#    return int(str(p) + str(m) + str(n))

# def returns_none():
#      x = 0

# print(returns_none())


# def euc_distance(x1, y1, x2, y2):
#     eu_dist = ((y2-y1)**2 + (x2-x1)**2)**(1/2)
#     return eu_dist



# def is_it_five(x):
#     if x == 5:
#         return True

# def five_or_three(x):
#     if x == 3:
#         return True
#     elif x == 5:
#         return True
#     else:
#         return False
# print(five_to_three(5))

# def special_or(expression1, expression2):
#     if not expression1 == True and not expression2 == True:
#         return False
#     return True
#     pass

# def is_either_even_or_are_both_7(num1, num2):
#     if num1 % 2 == 0 or num2 % 2 == 0:
#         return True
#     elif num1 == 7 and num2 == 7:
#         return True
#     else:
#         return False
#     pass
# print(is_either_even_or_are_both_7(3, 7))

# def is_either_even_and_less_than_9(num1, num2):
#     # your code here
#     if num1 % 2 == 0 or num2 % 2 == 0:
#         if num1 < 9 and num2 < 9:
#             return True
#         else:
#             return False
#     pass
# print(is_either_even_and_less_than_9(6, 10))

# def verify_ids(some_list1, some_list2):
#     return id(some_list1) == id(some_list2)

# def modify_third_elem(list1, x):
#     list1[2] = x
#     return list1

# def list_unpacker(lsr1):
#     a1, a2, a3 = lsr1
#     return a1, a2, a3

# lst1 = list(range(3))
# print(list_packer(lst1))

# def every_third_from_list(lst1):
#     third_item = lst1[2::3]
#     return third_item

# lst3 = []
# def append_three_elements(lst1, x, y, z):
#     new_lst = lst1[:]
#     new_lst.append(x)
#     new_lst.append(y)
#     new_lst.append(z)
#     return new_lst

# print(append_three_elements(lst3, 3, 4, 5))

# def extend_list(lst1, lst2, lst3):
#     new_lst = lst1[:]
#     new_lst.extend(lst2)
#     new_lst.extend(lst3)
#     return new_lst

# i_hate_lists = list(range(10))
# x = 3
# def remove_if_in_list(lst1, x):
#     new_list = lst1[:]
#     if x in new_list:
#         new_list.remove(x)
#         return new_list

# print(remove_if_in_list(i_hate_lists, x))

# bool_list = [True, False, True, True, False]
# print(any(bool_list))

# a = 10
# n = 20

# num_list = list(range(a, n))
# print(any(num_list))
# print(num_list)


# def here_we_go(list_1):

#     '''
#     Takes in a list, tosses it around a bit, and returns some outputs of some cool list operations.

#     Parameters:
#     ----------
#     list_1 : (list)
#         A list

#     Returns
#     ----------

#         1. The sorted version of the `list`.
#         2. The reversed version of the `list`.
#         3. The last element of the reversed `list` (without removing it from the `list`).
#         4. The number of times that the number 22 occurs in the `list`.

#     '''
#     reversed_copy = list(reversed(list_1))
#     pop_list = list(reversed(list_1))
#     sorted_copy = sorted(list_1)
#     last_item = pop_list.pop()
#     count_22 = list_1.count(22) 
    
#     return sorted_copy, reversed_copy, last_item, count_22
    

# # use x as the input to your function
# x = [22, 23, 4, 1, 22, 4, 6, 22, 2, 7, 88, 22]

# # call (and unpack) your function here 
# #print(here_we_go(x))
# sorted_copy, reversed_copy, last_item, count_22 = here_we_go(x)
# print(sorted_copy)
# print(reversed_copy)
# print(last_item)
# print(count_22)
# #print(x)


# total = 0
# for i in range(10):
#     total += i

# print(total)
# def accumulate(list_1):
#     '''
#     Returns an object that is the accumlated result of list_1.

#     Parameters:
#     ----------
#     list_1 : (list)
#         A list of strings.

#     Returns:
#     ----------
#         The accumulated version of the elements in the list.
#     '''
#     phrase = ''
#     for word in list_1:
#         phrase = phrase + word
#     return phrase
   

# # leave these lines alone
# x = ['python',' ','is',' ','cool', '.']
# result = accumulate(x)
# print(result)

# your_list = list(range(-10, 5))
# my_list = list(range(15))

# if len(your_list) == len(my_list):

#     gt_zero = False

#     for i in range(len(my_list)):

#         total = your_list[i] * my_list[i]

#         if total > 0:
#             gt_zero = True

#         if gt_zero:
#             print(i)
#             break


# put your code here
# evens = []
# odds =[]

# integers = list(range(1001))
# #print(integers)
# for i in integers:

#     if i % 2 == 0:
#         evens.append(i)
#     else:
#         odds.append(i)

# print(evens)
# print(odds)


# list_1 = list(range(100,501))
# num_accum = []
# idx_accum = []
# for idx, num in enumerate(list_1):
#     if num % 15 == 0:
#         num_accum.append(num)
#         idx_accum.append(idx)
# print(num_accum)
# print(idx_accum)

# def find_intersection(list1, list2):
#     '''
#     Returns the intersection of the two input lists.

#     Parameters:
#     ----------
#     list1 : (list)
#     list2 : (list)

#     Returns:
#     ----------
#     A list that contains the elements that are in both lists.
#     '''
#     both_list =[]
#     for element in list1:
#         for i in list2:
#             if element == i:
#                 both_list.append(i)
#     return both_list
# list_x = list(range(0,50,3))
# list_y = list(range(25,75,4))
# print(list_x)
# print(list_y)
# print(find_intersection(list_x, list_y))


# def nest_elements(list1, start_index, stop_index):
#     '''
#     Create a nested list within list1. Elements in [start_index, stop_index]
#     will be in the nested list.

#     Example:

#         >>> x = [1,2,3,4,5,6]
#         >>> y = nest_elements(x, 0, 4)
#         >>> print(y)
#         >>> [[1, 2, 3, 4, 5], 6]

#     Parameters:
#     ----------
#     list1 : (list)
#         A heterogeneous list.
#     start_index : (int)
#         The index of the first element that should be put into a nested list
#         (inclusive).
#     stop_index : (int)
#         The index of the last element that should be put into a nested list
#         (inclusive).

#     Returns:
#     ----------
#     A copy of list1, with the elements from start_index to stop_index in a
#     sub_list.
#     '''
#     return_list = []
#     nested_list = []
#     for idx, obj in enumerate(list1):
#         if idx >= start_index and idx <= stop_index:
#             nested_list.append(obj)
#             if idx == stop_index:
#                 return_list.append(nested_list)
#         else:
#             return_list.append(obj)
#     return return_list

# list1 = list(range(50))
# x = 7
# y = 25
# print(nest_elements(list1, x, y))

# def find_prime(list1):
#     '''
#     Finds all prime numbers within an input list and returns those primes
#     another list.

#     Parameters:
#     ----------
#     list1 : (list)
#         A list of integers.

#     Returns:
#     ----------
#     List of  all primes in list1 (if no primes are found, return the string
#     "No prime found.")
#     '''
    
#     prime_num = []
#     for num in list1:
#         prime = True
#         if num == 1:
#             prime = False
#         elif num == 2:
#             prime = True
#         else:
#             for n in range(2, int(num)):
#                 if num % n == 0:
#                     #print(f'   divisor:{n}')
#                     prime = False
#                     break
        
#         if prime == True:
#             prime_num.append(num)
        
#     if len(prime_num) > 0:
#         return prime_num
#     else:
#         return 'No prime found.'
#     #pass
#prime_list = [12,13,14,15,16,17,18,19,20,21,22,23]
#print(find_prime(prime_list))

# lst = []

# for i in range(20):
#     if i**2 >= 64 and i**2 <= 144:
#         continue
#     lst.append(i)

#     print(lst)

# def not_going(x):
#     if x == x:
#         pass
#     else:
#         print('wow')
#         return 
# print(not_going(5))        

# Leave this function alone
def is_prime(x):
    '''
    Determines if an input number is prime.

    Parameters:
    ----------
    x : (int)
        A positive integer.

    Returns:
    ----------
    True or False : (bool)
    '''
    if x == 1:
        return False
    elif x == 2:
        return True

    test = int(x/2) 
    while test >= 2:
        if x % test == 0:
            return False
        test -= 1

    return True
#print(is_prime(9))

# # def find_primes(n):
# #     '''
# #     Finds all prime numbers up to (and potentially including) an input number
# #     and returns all the prime numbers in a list. In the rare case that there
# #     are no prime number between 0 and n, the function will return an empty list.

# #     Parameters:
# #     ----------
# #     n : (int)
# #         A positive integer.

# #     Returns:
# #     ----------
# #     list of primes : (list)
# #     '''
# #     pass