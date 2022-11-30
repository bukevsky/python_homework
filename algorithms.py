import random

RAND_MAX = 100

def generate_list(number_of_elements):
    list_ = [0] * number_of_elements
    for index in range(number_of_elements):
        list_[index] = random.randint(-RAND_MAX, RAND_MAX)
    return list_


def Bubble_Sort(list_):
    for run in range(len(list_)-1):
        for i in range(len(list_)-1-run):
            if list_[i]>list_[i+1]:
                list_[i],list_[i+1] = list_[i+1],list_[i]
    return list_


def selection_sort(list_):
    for i in range(len(list_)):
        mn = i
        for j in range(i,len(list_)):
            if list_[mn] > list_[j]:
                mn = j
        list_[i], list_[mn] = list_[mn], list_[i]
    return list_


def insertion_sort(list_):
    for i in range(1,len(list_)):
        for j in range(i,0,-1):
            if list_[j] < list_[j-1]:
                list_[j], list_[j-1] = list_[j-1], list_[j]
            else:
                break
    return list_


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

def merge_sort(s):
    if len(s) == 1:
        return s
    mid = len(s) // 2
    left_list = merge_sort(s[:mid])
    right_list = merge_sort(s[mid:])
    return merge(left_list, right_list)





