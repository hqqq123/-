def binary_search(list1,num):
    left=0
    right=len(list1)-1

    while left <= right:
        middle = (left + right) // 2
        if list1[middle]<num:
            left=middle+1
        elif list1[middle]>num:
            right=middle-1
        elif list1[middle]==num:
            return middle
    return -1
if __name__ == '__main__':
    list1=[1,2,3,4]
    index=binary_search(list1,2)
    print(index)
