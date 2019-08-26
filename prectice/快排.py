
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


if __name__ == '__main__':
    nums=[6,1,7,9,5,8,2,4,3]
    quick_sort(nums,0,8)
    print(nums)


