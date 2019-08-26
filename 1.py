import random
import threading
from queue import Queue


def add(li,queue,lock):
    lock.acquire()
    queue.put(sum(li))
    lock.release()
if __name__ == '__main__':
    threadCount=5
    li=[random.randint(1,100) for i in range(random.randint(1024,1024*1024))]

    lock=threading.Lock()
    threads=[]
    k1=0
    q=Queue()
    length=len(li)//threadCount
    for i in range(threadCount):
        k2=k1+length
        t=threading.Thread(target=add,args=(li[k1:k2],q,lock))
        t.start()
        threads.append(t)
        k1=k2
    if k2<len(li):
        t=threading.Thread(target=add,args=(li[k2:len(li)],q,lock))
        t.start()
        threads.append(t)
        threadCount+=1
    [i.join() for i in threads]
    res=0
    for i in range(threadCount):
        res+=q.get()


    print(res)
    print('-------对比结果是否正确--------')
    print(sum(li))