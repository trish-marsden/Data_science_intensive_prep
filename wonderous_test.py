# write your code here
def wondrous_test(n):
    '''
    If n is odd, triple it and add one. If n is even, take half of it. Repeat
    this process until the number 1 is reached. Return a list of all numbers
    that were iterated through.

    Parameters:
    ----------
    n : (int)
        A positive integer.

    Returns:
    ----------
    (list) of integers
    '''
    nums = [n]
    while n != 1:
        if n % 2 == 0:
            n = n/2 
        else:
            n = n * 3 + 1
        nums.append(n)
    return nums
print(wondrous_test(10))
    #pass
