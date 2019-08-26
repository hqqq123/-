import random
import threading

import time
def timeit(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = f(*args, **kwargs)
        end_time = time.time()
        print("%s函数运行时间:%.6f" % (f.__name__, end_time - start_time))
        return res
    return wrapper

def Midian3(nums,l,r):
    if r-l+1<=2:
        if nums[l] > nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
        return nums[l]
    m=(l+r)//2
    if nums[l]>nums[r]:
        nums[l],nums[r]=nums[r],nums[l]
    if nums[l]>nums[m]:
        nums[l],nums[m]=nums[m],nums[l]
    if nums[m] > nums[r]:
        nums[m],nums[r]=nums[r],nums[m]
    nums[m],nums[r-1]=nums[r-1],nums[m]
    return nums[r-1]

def quick_sort(nums,left,right):
    pivot=Midian3(nums,left,right)
    if right-left+1>2:
        i=left+1
        j=right-2
        while True:
            while nums[i]<pivot:
                i+=1
            while nums[j]>pivot:
                j-=1
            if i<j:
                nums[i],nums[j]=nums[j],nums[i]
            else:
                break
        nums[i],nums[right-1]=nums[right-1],nums[i]
        quick_sort(nums,left,i-1)
        quick_sort(nums,i+1,right)
@timeit
def use_thread(nums):

    mid = len(nums) // 2
    t1 = threading.Thread(target=quick_sort, args=(nums, 0, mid))

    t2 = threading.Thread(target=quick_sort, args=(nums, mid + 1, len(nums) - 1))
    t1.start()

    t2.start()
    t1.join()
    t2.join()
    # quick_sort(nums, 0, 8)
    a = nums[0:mid + 1]
    b = nums[mid + 1:]
    # print(a)
    # print(b)
    i = 0
    j = 0
    res = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    while i < len(a):
        res.append(a[i])
        i += 1
    while j < len(b):
        res.append(b[j])
        j += 1
    # print(res)
@timeit
def no_use_thread(nums):
    quick_sort(nums,0,len(nums)-1)
if __name__ == '__main__':
    nums = [random.randint(1, 100) for i in range(1024)]
    use_thread(nums)
    no_use_thread(nums)