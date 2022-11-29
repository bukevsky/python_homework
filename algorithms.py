import random

RAND_MAX = 100

def generate_list(number_of_elements):
    list_ = [0] * number_of_elements
    for index in range(number_of_elements):
        list_[index] = random.randint(-RAND_MAX, RAND_MAX)
    return list_


def insertion_sort(list_):
    for i in range(1,len(list_)):
        for j in range(i,0,-1):
            if list_[j] < list_[j-1]:
                list_[j], list_[j-1] = list_[j-1], list_[j]
            else:
                break
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



