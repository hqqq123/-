import random
import threading


def Merge(nums,nums2,left,right,rightEnd,lock):
    leftEnd=right-1
    start=left
    index=left
    while left<=leftEnd and right<=rightEnd:
        if nums[left]<nums[right]:
            lock.acquire()
            nums2[index]=nums[left]
            index+=1
            left+=1
            lock.release()

        else:
            lock.acquire()
            nums2[index]=nums[right]
            index+=1
            right+=1
            lock.release()

    while left<=leftEnd:
        lock.acquire()

        nums2[index] = nums[left]
        index += 1
        left+=1
        lock.release()

    while right<=rightEnd:
        lock.acquire()

        nums2[index] = nums[right]
        index += 1
        right+=1
        lock.release()

    while rightEnd>=start:
        lock.acquire()

        nums[rightEnd]=nums2[rightEnd]
        rightEnd-=1
        lock.release()


def MergeSort(nums,nums2,left,rightEnd,lock):

    if left<rightEnd:
        center=(left+rightEnd)//2
        MergeSort(nums,nums2,left,center,lock)
        MergeSort(nums,nums2,center+1,rightEnd,lock)
        Merge(nums,nums2,left,center+1,rightEnd,lock)

if __name__ == '__main__':
    nums=[random.randint(1,1024) for i in range(1024)]
    nums2=[random.randint(1,1024) for i in range(1024)]
    lock=threading.Lock()
    t1=threading.Thread(target=MergeSort,args=(nums,nums2,0,len(nums)//2,lock))
    t2=threading.Thread(target=MergeSort,args=(nums,nums2,len(nums)//2+1,len(nums)-1,lock))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    Merge(nums,nums2,0,len(nums)//2+1,len(nums)-1,lock)
    # print(nums)
    print(len(nums))