import random
import time

NUMBER_OF_ELEMENTS_IN_TEST_LIST = 10000
NUMBER_OF_TESTS = 10
RAND_MAX = 1000


def generate_list(number_of_elements):
    list_ = [0] * number_of_elements
    for index in range(number_of_elements):
        list_[index] = random.randint(-RAND_MAX, RAND_MAX)
    return list_


def test(func):
    total_timer = 0
    for test_number in range(NUMBER_OF_TESTS):
        test_list = generate_list(NUMBER_OF_ELEMENTS_IN_TEST_LIST)
        timer = time.time()
        test_list = func(test_list)
        timer = time.time() - timer
        total_timer += timer
        if sort_check(test_list):
            print("Required time in test №", test_number + 1, "is", timer, "seconds")
        else:
            print("Error in test №", test_number + 1)
    print("Required time for", NUMBER_OF_TESTS, "tests is", total_timer, "seconds")
    print("Average time for", NUMBER_OF_TESTS, "tests is", total_timer / NUMBER_OF_TESTS, "seconds")


def sort_check(list_):
    for index in range(len(list_) - 1):
        if list_[index] > list_[index + 1]:
            return False
    return True


# --------------------------------------------------------------------

def bubble_sort(list_):  # 0(n**2)
    for run in range(len(list_) - 1):
        for i in range(
                len(list_) - 1 - run):  # run для того, чтобы не проверять последние элементы списка(лишние проверки).
            if list_[i] > list_[i + 1]:
                list_[i], list_[i + 1] = list_[i + 1], list_[i]
    return list_


# --------------------------------------------------------------------

def selection_sort(list_):  # 0(n**2)
    for i in range(len(list_)):
        mn = i
        for j in range(i, len(list_)):
            if list_[mn] > list_[j]:
                mn = j
        list_[i], list_[mn] = list_[mn], list_[i]
    return list_


# --------------------------------------------------------------------

def insertion_sort(list_):
    for i in range(1, len(list_)):
        for j in range(i, 0, -1):
            if list_[j] < list_[j - 1]:
                list_[j], list_[j - 1] = list_[j - 1], list_[j]
            else:
                break
    return list_


# --------------------------------------------------------------------

def merge(a, b):
    sorted_list = []
    i = j = 0
    while i < (len(a)) and j < (len(b)):
        if a[i] < b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1
    if i < len(a):
        sorted_list += a[i:]
    if j < len(b):
        sorted_list += b[j:]
    return sorted_list


def merge_sort(list_):
    if len(list_) == 1:
        return list_
    mid = len(list_) // 2
    left_list = merge_sort(list_[:mid])
    right_list = merge_sort(list_[mid:])
    return merge(left_list, right_list)


# --------------------------------------------------------------------

def quick_sort(list_):
    if len(list_) <= 1:  # Выход с рекурсии
        return list_
    elem = list_[0]  # Опорный элемент
    left = [i for i in list_ if i < elem]
    center = [i for i in list_ if i == elem]
    right = [i for i in list_ if i > elem]
    return quick_sort(left) + center + quick_sort(right)


# --------------------------------------------------------------------

def binary_search(list_, value, start, end):
    if start == end:
        if list_[start] > value:
            return start
        else:
            return start + 1
    elif start > end:
        return start
    middle = (start + end) // 2
    if list_[middle] < value:
        return binary_search(list_, value, middle + 1, end)
    elif list_[middle] > value:
        return binary_search(list_, value, start, middle - 1)
    else:
        return middle


def binary_insert_sort(array):
    sorted_array = array.copy()
    for i in range(1, len(sorted_array)):
        value = sorted_array[i]
        j = binary_search(sorted_array, value, 0, i - 1)
        sorted_array = sorted_array[:j] + [value] + sorted_array[j:i] + sorted_array[i + 1:]
    return sorted_array
