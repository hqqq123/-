def rev(num):
    num=str(num)[::-1]

    return num

if __name__ == '__main__':
    for i in range(256):
        if i*i==int(rev(i * i)):
            print(i)