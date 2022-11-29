import random

RAND_MAX = 100

def generate_list(number_of_elements):
    list_ = [0] * number_of_elements
    for index in range(number_of_elements):
        list_[index] = random.randint(-RAND_MAX, RAND_MAX)
    return list_
s = [2, -3, 5, 8, 3, 9, -11, -7]
# sorted [-11, -7, -3, 2, 3, 5, 8, 9]


def insertion(list_):
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

print(Bubble_Sort(generate_list(10)))




