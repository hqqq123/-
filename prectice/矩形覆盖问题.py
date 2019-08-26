def circle_fib(n):
    f1=0
    f2=1
    for i in range(n):
        f1,f2=f2,f1+f2
    return f2
if __name__ == '__main__':
    n=4
    print(circle_fib(n))