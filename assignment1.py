# Course: CS261 - Data Structures
# Student Name: Jason Marsh
# Assignment: 1
# Description:

import random
import string
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------


def min_max(arr: StaticArray) -> ():
    """Take StaticArray object as input, return tuple of minimum and maximum value of array"""
    array_min = arr[0]
    array_max = arr[0]
    for val in range(0, arr.size()):
        if arr[val] < array_min:
            array_min = arr[val]
        if arr[val] > array_max:
            array_max = arr[val]
    return array_min, array_max


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------


def fizz_buzz(arr: StaticArray) -> StaticArray:
    """Receives a StaticArray of integers and returns a new StaticArray object
    based on the original array. If the value from the original array is divisible
    by 3 and 5, the value in the new array is 'fizzbuzz', if it's divisible by
    3 but not 5, 'fizz', and if it's divisible by 5 but not 3, 'buzz'. If it's
    divisible by neither 3 nor 5, the value will be the same as that in the
    original array.
    """
    newArr = StaticArray(arr.size())
    for val in range(0, arr.size()):
        if arr[val] % 3 == 0 and arr[val] % 5 == 0:
            newArr[val] = 'fizzbuzz'
        elif arr[val] % 3 == 0:
            newArr[val] = 'fizz'
        elif arr[val] % 5 == 0:
            newArr[val] = 'buzz'
        else:
            newArr[val] = arr[val]
    return newArr


# ------------------- PROBLEM 3 - REVERSE -----------------------------------


def reverse(arr: StaticArray) -> None:
    """Reverse a StaticArray object in place"""
    left = 0
    while left < (arr.size() - 1)/2:
        temp = arr[arr.size() - 1 - left]
        arr[arr.size() - 1 - left] = arr[left]
        arr[left] = temp
        left += 1
    return


# ------------------- PROBLEM 4 - ROTATE ------------------------------------


def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """Function that receives two parameters - a StaticArray and an integer value (called
    steps). The function will create and return a new StaticArray, where all elements are from
    the original array but their position has shifted right or left steps number of times.
    """
    new_arr = StaticArray(arr.size())
    move_right = True
    if steps < 0:
        move_right = False
        # Make steps positive after setting boolean
        steps = steps - (steps * 2)
    if steps > arr.size():
        # Reduce number of steps required by finding remaining steps after
        # dividing steps by array size
        steps = steps % arr.size()
    if move_right:
        for val in range(0, arr.size()):
            new_place = val + steps
            if new_place >= arr.size():
                new_place -= arr.size()
            new_arr[new_place] = arr[val]
    else:
        for val in range(0, arr.size()):
            new_place = val - steps
            if new_place < 0:
                new_place += arr.size()
            new_arr[new_place] = arr[val]
    return new_arr


# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------


def sa_range(start: int, end: int) -> StaticArray:
    """Function that receives two integers start and end and returns a StaticArray that
    contains all consecutive values between start and end (inclusive).
    """
    # Check if we need to count forwards (end > start) or backwards (start > end)
    # If start = end, this is handled in else statement
    if end > start:
        arr = StaticArray(end - start + 1)
        for val in range(0, arr.size()):
            arr[val] = start + val
    else:
        arr = StaticArray(start - end + 1)
        for val in range(0,arr.size()):
            arr[val] = start - val
    return arr


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------


def is_sorted(arr: StaticArray) -> int:
    """Function that receives a StaticArray and returns an integer that describes whether
    the array is sorted. Integers returned are as follows:
    1: Strictly ascending (or only contains one element)
    2: Strictly descending
    0: Neither strictly ascending nor descending
    """
    # Handle case where array contains a single element
    if arr.size() == 1:
        return 1
    # Based on first two elements, check if we should verify if array is ascending or descending
    if arr[1] > arr[0]:
        ascending = True
    else:
        ascending = False
    for val in range(0, arr.size()):
        # If we have made it all the way through the array, return 1 or 2 depending on condition met
        if val + 1 == arr.size():
            if ascending:
                return 1
            elif not ascending:
                return 2
        # If still iterating through array, check if next element goes in opposite direction, return 0 if so
        elif ascending:
            if arr[val+1] <= arr[val]:
                return 0
        elif not ascending:
            if arr[val+1] >= arr[val]:
                return 0


# ------------------- PROBLEM 7 - SA_SORT -----------------------------------


def sa_sort(arr: StaticArray) -> None:
    """ Function that receives a StaticArray and sorts its content in non-descending order.
    Original array is modified, nothing is returned
    """
    sorted = True
    for val in range(0, arr.size()):
        for val2 in range(0, arr.size() - val - 1):
            if arr[val2] > arr[val2 + 1]:
                temp = arr[val2]
                arr[val2] = arr[val2 + 1]
                arr[val2 + 1] = temp
                sorted = False
        if sorted:
            break
    return


# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------


def remove_duplicates(arr: StaticArray) -> StaticArray:
    """Function that receives a StaticArray where the elements are already in sorted order
    and returns a new StaticArray with duplicate values removed.
    """
    duplicates = 0
    for val in range(1, arr.size()):
        if arr[val] == arr[val - 1]:
            duplicates += 1

    new_arr = StaticArray(arr.size() - duplicates)
    new_arr[0] = arr[0]

    count = 1
    for val in range(1, arr.size()):
        if arr[val] != arr[val - 1]:
            new_arr[count] = arr[val]
            count += 1
    return new_arr



# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------


def count_sort(arr: StaticArray) -> StaticArray:
    """Function that receives a StaticArray and returns a new StaticArray with the same
    content sorted in non-ascending order. The original array should not be modified.
    Uses radix sort
    """
    min_value = min_max(arr)[0]
    max_value = min_max(arr)[1]
    new_arr = StaticArray(arr.size())
    count = StaticArray(max_value - min_value + 1)

    for val in range(0, count.size()):
        count[val] = 0

    for val in range(0, arr.size()):
        count[count.size() - (arr[val] - min_value) - 1] += 1

    for val in range(1, count.size()):
        count[val] = count[val] + count[val-1]

    for val in range(0, new_arr.size()):
        new_arr[count[count.size() - (arr[val] - min_value) - 1] - 1] = arr[val]
        count[count.size() - (arr[val] - min_value) - 1] -= 1

    return new_arr


# ------------------- PROBLEM 10 - SA_INTERSECTION --------------------------


def sa_intersection(arr1: StaticArray, arr2: StaticArray, arr3: StaticArray) \
        -> StaticArray:
    """Function that receives three StaticArrays where the elements are already in sorted
    order and returns a new StaticArray with only those elements that appear in all three input
    arrays
    """
    return sa_intersection_helper(sa_intersection_helper(arr1, arr2), arr3)


def sa_intersection_helper(arr1: StaticArray, arr2: StaticArray) \
        -> StaticArray:
    """Helper function for sa_intersection"""
    count = 0
    index1 = 0
    index2 = 0

    if arr1[0] is None or arr2[0] is None:
        new_arr = StaticArray(1)
        return new_arr

    while index1 < arr1.size() and index2 < arr2.size():
        if arr1[index1] > arr2[index2]:
            index2 += 1
        elif arr2[index2] > arr1[index1]:
            index1 += 1
        else:
            index1 += 1
            index2 += 1
            count += 1

    if count == 0:
        new_arr = StaticArray(1)
        return new_arr

    new_arr = StaticArray(count)
    index1 = 0
    index2 = 0
    count = 0

    while index1 < arr1.size() and index2 < arr2.size():
        if arr1[index1] > arr2[index2]:
            index2 += 1
        elif arr2[index2] > arr1[index1]:
            index1 += 1
        else:
            new_arr[count] = arr1[index1]
            index1 += 1
            index2 += 1
            count += 1
    return new_arr


# ------------------- PROBLEM 11 - SORTED SQUARES ---------------------------


def sorted_squares(arr: StaticArray) -> StaticArray:
    """Function that receives a StaticArray where the elements are already in sorted order
    and returns a new StaticArray with squares of the values from the original array, sorted in
    non-descending order.
    """
    new_arr = StaticArray(arr.size())

    left = 0
    right = arr.size() - 1

    for val in range(0, arr.size()):
        if abs(arr[left]) >= abs(arr[right]):
            new_arr[arr.size() - 1 - val] = arr[left] ** 2
            left += 1
        else:
            new_arr[arr.size() - 1 - val] = arr[right] ** 2
            right -= 1

    return new_arr



# ------------------- PROBLEM 12 - ADD_NUMBERS ------------------------------


def add_numbers(arr1: StaticArray, arr2: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    pass


# ------------------- PROBLEM 13 - SPIRAL MATRIX -------------------------


def spiral_matrix(rows: int, cols: int, start: int) -> StaticArray:
    """
    TODO: Write this implementation
    """
    pass


# ------------------- PROBLEM 14 - TRANSFORM_STRING -------------------------


def transform_string(source: str, s1: str, s2: str) -> str:
    """
    TODO: Write this implementation
    """
    pass


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    # print('\n# min_max example 1')
    # arr = StaticArray(5)
    # for i, value in enumerate([7, 8, 6, -5, 4]):
    #     arr[i] = value
    # print(min_max(arr))
    #
    #
    # print('\n# min_max example 2')
    # arr = StaticArray(1)
    # arr[0] = 100
    # print(min_max(arr))
    #
    #
    # print('\n# min_max example 3')
    # test_cases = (
    #     [3, 3, 3],
    #     [-10, -30, -5, 0, -10],
    #     [25, 50, 0, 10],
    # )
    # for case in test_cases:
    #     arr = StaticArray(len(case))
    #     for i, value in enumerate(case):
    #         arr[i] = value
    #     print(min_max(arr))
    #
    #
    # print('\n# fizz_buzz example 1')
    # source = [_ for _ in range(-5, 20, 4)]
    # arr = StaticArray(len(source))
    # for i, value in enumerate(source):
    #     arr[i] = value
    # print(fizz_buzz(arr))
    # print(arr)
    #
    #
    # print('\n# reverse example 1')
    # source = [_ for _ in range(-20, 20, 7)]
    # arr = StaticArray(len(source))
    # for i, value in enumerate(source):
    #     arr.set(i, value)
    # print(arr)
    # reverse(arr)
    # print(arr)
    # reverse(arr)
    # print(arr)
    #
    #
    # print('\n# rotate example 1')
    # source = [_ for _ in range(-20, 20, 7)]
    # arr = StaticArray(len(source))
    # for i, value in enumerate(source):
    #     arr.set(i, value)
    # print(arr)
    # for steps in [1, 2, 0, -1, -2, 28, -100, 2**28, -2**31]:
    #     print(rotate(arr, steps), steps)
    # print(arr)
    #
    #
    # # print('\n# rotate example 2')
    # # array_size = 1_000_000
    # # source = [random.randint(-10**9, 10**9) for _ in range(array_size)]
    # # arr = StaticArray(len(source))
    # # for i, value in enumerate(source):
    # #     arr[i] = value
    # # print(f'Started rotating large array of {array_size} elements')
    # # rotate(arr, 3**14)
    # # rotate(arr, -3**15)
    # # print(f'Finished rotating large array of {array_size} elements')
    #
    #
    # print('\n# sa_range example 1')
    # cases = [
    #     (1, 3), (-1, 2), (0, 0), (0, -3),
    #     (-105, -99), (-99, -105)]
    # for start, end in cases:
    #     print(start, end, sa_range(start, end))
    #
    #
    # print('\n# is_sorted example 1')
    # test_cases = (
    #     [-100, -8, 0, 2, 3, 10, 20, 100],
    #     ['A', 'B', 'Z', 'a', 'z'],
    #     ['Z', 'T', 'K', 'A', '5'],
    #     [1, 3, -10, 20, -30, 0],
    #     [-10, 0, 0, 10, 20, 30],
    #     [100, 90, 0, -90, -200],
    #     ['apple']
    # )
    # for case in test_cases:
    #     arr = StaticArray(len(case))
    #     for i, value in enumerate(case):
    #         arr[i] = value
    #     print('Result:', is_sorted(arr), arr)
    #
    #
    # # print('\n# sa_sort example 1')
    # # test_cases = (
    # #     [1, 10, 2, 20, 3, 30, 4, 40, 5],
    # #     ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
    # #     [(1, 1), (20, 1), (1, 20), (2, 20)],
    # #     [random.randint(-10**7, 10**7) for _ in range(5_000)]
    # # )
    # # for case in test_cases:
    # #     arr = StaticArray(len(case))
    # #     for i, value in enumerate(case):
    # #         arr[i] = value
    # #     print(arr if len(case) < 50 else 'Started sorting large array')
    # #     sa_sort(arr)
    # #     print(arr if len(case) < 50 else 'Finished sorting large array')
    #
    #
    # print('\n# remove_duplicates example 1')
    # test_cases = (
    #     [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
    #     [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    # )
    # for case in test_cases:
    #     arr = StaticArray(len(case))
    #     for i, value in enumerate(case):
    #         arr[i] = value
    #     print(arr)
    #     print(remove_duplicates(arr))
    # print(arr)
    #
    #
    # print('\n# count_sort example 1')
    # test_cases = (
    #     [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
    #     [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
    #     [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    # )
    # for case in test_cases:
    #     arr = StaticArray(len(case))
    #     for i, value in enumerate(case):
    #         arr[i] = value
    #     print(arr if len(case) < 50 else 'Started sorting large array')
    #     result = count_sort(arr)
    #     print(result if len(case) < 50 else 'Finished sorting large array')


    # print('\n# count_sort example 2')
    # array_size = 5_000_000
    # min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    # max_val = min_val + 998
    # case = [random.randint(min_val, max_val) for _ in range(array_size)]
    # arr = StaticArray(len(case))
    # for i, value in enumerate(case):
    #     arr[i] = value
    # print(f'Started sorting large array of {array_size} elements')
    # result = count_sort(arr)
    # print(f'Finished sorting large array of {array_size} elements')


    print('\n# sa_intersection example 1')
    test_cases = (
        ([1, 2, 3], [3, 4, 5], [2, 3, 4]),
        ([1, 2], [2, 4], [3, 4]),
        ([1, 1, 2, 2, 5, 75], [1, 2, 2, 12, 75, 90], [-5, 2, 2, 2, 20, 75, 95]),
        ([-9, 3, 5, 5, 6, 8, 8, 10],[-10, -6, -5, -3, -2, 0, 2, 4, 8, 9],[-4, -3, 1, 1, 3, 3, 4, 6, 8, 9])
    )
    for case in test_cases:
        arr = []
        for i, lst in enumerate(case):
            arr.append(StaticArray(len(lst)))
            for j, value in enumerate(sorted(lst)):
                arr[i][j] = value
        print(sa_intersection(arr[0], arr[1], arr[2]))


    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)


    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10**9, 10**9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')


    print('\n# add_numbers example 1')
    test_cases = (
        ([1, 2, 3], [4, 5, 6]),
        ([0], [2, 5]), ([0], [0]),
        ([2, 0, 9, 0, 7], [1, 0, 8]),
        ([9, 9, 9], [9, 9, 9, 9])
    )
    for num1, num2 in test_cases:
        n1 = StaticArray(len(num1))
        n2 = StaticArray(len(num2))
        for i, value in enumerate(num1):
            n1[i] = value
        for i, value in enumerate(num2):
            n2[i] = value
        print('Original nums:', n1, n2)
        print('Sum: ', add_numbers(n1, n2))


    print('\n# spiral matrix example 1')
    matrix = spiral_matrix(1, 1, 7)
    print(matrix)
    if matrix: print(matrix[0])
    matrix = spiral_matrix(3, 2, 12)
    if matrix: print(matrix[0], matrix[1], matrix[2])


    print('\n# spiral matrix example 2')
    def print_matrix(matrix: StaticArray) -> None:
        rows, cols = matrix.size(), matrix[0].size()
        for row in range(rows):
            for col in range(cols):
                print('{:4d}'.format(matrix[row][col]), end=' ')
            print()
        print()

    test_cases = (
        (4, 4, 1), (3, 4, 0), (2, 3, 10), (1, 2, 1), (1, 1, 42),
        (4, 4, -1), (3, 4, -3), (2, 3, -12), (1, 2, -42),
    )
    for rows, cols, start in test_cases:
        matrix = spiral_matrix(rows, cols, start)
        if matrix: print_matrix(matrix)


    print('\n# transform_strings example 1')
    test_cases = ('eMKCPVkRI%~}+$GW9EOQNMI!_%{#ED}#=-~WJbFNWSQqDO-..@}',
                  'dGAqJLcNC0YFJQEB5JJKETQ0QOODKF8EYX7BGdzAACmrSL0PVKC',
                  'aLiAnVhSV9}_+QOD3YSIYPR4MCKYUF9QUV9TVvNdFuGqVU4$/%D',
                  'zmRJWfoKC5RDKVYO3PWMATC7BEIIVX9LJR7FKtDXxXLpFG7PESX',
                  'hFKGVErCS$**!<OS<_/.>NR*)<<+IR!,=%?OAiPQJILzMI_#[+}',
                  'EOQUQJLBQLDLAVQSWERAGGAOKUUKOPUWLQSKJNECCPRRXGAUABN',
                  'WGBKTQSGVHHHHHTZZZZZMQKBLC66666NNR11111OKUN2KTGYUIB',
                  'YFOWAOYLWGQHJQXZAUPZPNUCEJABRR6MYR1JASNOTF22MAAGTVA',
                  'GNLXFPEPMYGHQQGZGEPZXGJVEYE666UKNE11111WGNW2NVLCIOK',
                  'VTABNCKEFTJHXATZTYGZVLXLAB6JVGRATY1GEY1PGCO2QFPRUAP',
                  'UTCKYKGJBWMHPYGZZZZZWOKQTM66666GLA11111CPF222RUPCJT')
    for case in test_cases:
        print(transform_string(case, '612HZ', '261TO'))
