def get_huiwen(str):
    t=['$','#']
    for i in str:
        t.append(i)
        t.append('#')
    t.append('*')
    print(t)
    id=0
    mx=0
    length=0
    index=0
    p=[0 for i in range(len(t)+1)]
    for i in range(1,len(t)-1):
        if mx>i:
            if mx-i>p[2*id-i]:
                p[i]=p[2*id-i]
            else:
                p[i]=mx-i
        else:
            p[i]=1
        while(t[i+p[i]]==t[i-p[i]]):
            p[i]+=1
        if mx<i+p[i]:
            mx=i+p[i]
            id=i
        if length<p[i]:
            length=p[i]
            index=i
    print(p)
    return t[index-length+2:index+length-1:2]


if __name__ == '__main__':
    print(get_huiwen('12212321'))