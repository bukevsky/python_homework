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

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)
    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    return merge(left_list, right_list)


random_list_ = generate_list(100)
print(merge_sort(random_list_))
