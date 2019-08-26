def find_min(li):
    if len(li)>0:
        min=11111
        left=0
        right=len(li)-1
        middle=left
        while li[left]>=li[right]:
            if right-left==1:
                middle=right
                break
            middle=(left+right)//2
            if li[middle]>li[right]:
                left=middle
            if li[middle]<li[right]:
                right=middle
        return li[middle]
    else:
        return 0
if __name__ == '__main__':
    li=[4,5,6,7,8,9,1,2,3]
    print(min(li))
    print(find_min(li))

