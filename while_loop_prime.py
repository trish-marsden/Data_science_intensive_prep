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
#print(is_prime(173))

def find_primes(n):
    '''
    Finds all prime numbers up to (and potentially including) an input number
    and returns all the prime numbers in a list. In the rare case that there
    are no prime number between 0 and n, the function will return an empty list.

    Parameters:
    ----------
    n : (int)
        A positive integer.

    Returns:
    ----------
    list of primes : (list)
    '''
    """
    this code is wrong and way to complicated
    """
    # prime_list = []
    # n_list = list(range(0, n))
    # k = len(n_list)
    # while k > 0:
    #     Prime = False
    #     Prime = is_prime(n_list[k-1])
        
    #     if Prime:
    #         prime_list.append(n_list[k-1])
    #         k -= 1
    #     else:
    #         k -= 1
    #         continue
    # prime_list.reverse()
    # return prime_list

    num = 2
    list_of_prime = []
    
    while num <= n:
        if is_prime(num):
            list_of_prime.append(num)
        num += 1
    return list_of_prime
#test_list = [12, 11, 54, 113, 2, 3, 13, 46, 173, 6, 3, 12, 3, 4, 543, 54]
#test_list = 100
#print(find_primes(test_list))




   