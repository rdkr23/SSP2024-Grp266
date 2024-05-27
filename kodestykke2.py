def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process

    # Traverse through all array elements
    for i in range(n - 1):
        swapped = True
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j + 1] < arr[j]:
                swapped = False
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return


# White test:
# [-20, 2] --> -20  2
# [2, -20] --> -20  2

# Black box test:
# 0: Fail: TypeError: object of type 'int' has no len()
# "h" Fail: TypeError: %d format: a number is required, not str
# None Fail: TypeError: object of type 'NoneType' has no len()
# 2.5911 Fail: TypeError: object of type 'float' has no len()
# -2.5911 Fail: TypeError: object of type 'float' has no len()
# 2 Fail: TypeError: object of type 'int' has no len()
# -2 Fail: TypeError: object of type 'int' has no len()
# False Fail Fail: TypeError: object of type 'bool' has no len()
# True Fail Fail: TypeError: object of type 'bool' has no len()
# [3,1,1,5]  1  1  3  5
# {"a": 1, "b": 2} Fail: KeyError: 1
# [3.1,1.3,1.5,5.8]  [1.3, 1.5, 3.1, 5.8]
# ["a", "d", "c", "b"] ['a', 'b', 'c', 'd']
# ["adwd", "acwd", "abwd", "aawd"] ['aawd', 'abwd', 'acwd', 'adwd']
# [False, True, True, False] [False, False, True, True]
# [None, None, None, None] Fail: TypeError: '<' not supported between instances of 'NoneType' and 'NoneType'
# [3.1, "agd", False, 3] Fail: TypeError: '<' not supported between instances of 'str' and 'float'
# [3.1, 3, 2.4, 7] [2.4, 3, 3.1, 7]


# Driver code to test above
arr = [3.1, 3, 2.4, 7]

bubbleSort(arr)

print(arr)
