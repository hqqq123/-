def get_yinzi(num):
    t=0
    for i in range(1,num//2+1):
        if num%i==0:
            t+=i

    return t
if __name__ == '__main__':
    w=''
    y=''
    for i in range(2,61):
        t=0
        if get_yinzi(i)==i:
            w += ' '
            w+=str(i)

        if get_yinzi(i)>i:
            y+=' '
            y+=str(i)
    print('E:'+w+'(ei 为完数) G:'+y+'(gi 为盈数)')
