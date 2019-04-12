import math
def binary_search(list,item):
    low = 0
    hight = len(list) -1
    while low<=hight:
        mid = math.ceil((hight+low)/2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            hight = mid -1
        if guess < item:
            low = mid + 1
    return None

my_list = [1,3,4,5,6,7,8,9]

res = binary_search(my_list,8)

print (res)