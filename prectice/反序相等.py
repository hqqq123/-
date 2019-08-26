def rev(num):
    num=str(num)[::-1]
    return num
if __name__ == '__main__':
    for i in range(1000,10000):
        if i==int(rev(i*9)):
            print(i)