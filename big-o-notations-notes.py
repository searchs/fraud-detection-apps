# Big O Notation Examples


# Constant Time - O(1)
def get_first(item_list):
    """The algorithm takes the same amount of time to run,
    independent the size of input data
    """
    return item_list[0]


# Linear Time - O(n)
def get_sum(nums_list):
    """The execution time is directly proportional to the size of
    the input.  The number of iterations of the main loop
    increases linearly with an increasing value of n
    """
    sum = 0
    for item in nums_list:
        sum = sum + item
    return sum


# Quadratic Time - O(n2)
# Using a two-dimensional array as input
def get_sum_dim(dim_arr_list):
    """The execution time of the algorithm is proportional
    to the square of the input size.
    The nested loop gives the algorithm teh complexity of O(n2)
    e.g. Bubble sort algorithm
    """
    sum = 0
    for row in dim_arr_list:
        for item in row:
            sum += item
    return sum


# Logarithm time - O(logn)


def binary_search(src_list, item):
    """The execution time of the algorithm is proportional
    to the logarithm of the input size.
    Ordered list assumed.
    Verdict: Gold Standard
    """
    first = 0
    last = len(src_list) - 1
    found_flag = False
    while first <= last and not found_flag:
        mid = (first + last) // 2
        if src_list[mid] == item:
            found_flag = True
        else:
            if item < src_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found_flag
