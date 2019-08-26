def replace_str(str):
    space_num=0
    for i in str:
        if i==' ':
            space_num+=1
    raw_len=len(str)
    new_len=raw_len+space_num*2
    raw=raw_len-1
    new=new_len-1
    while raw!=new:
        if str[raw]==' ':
            str[new]='%'
            str[new-1]='0'
            str[new-2]='2'
            new-=3
        else:
            str[new]=str[raw]
            new-=1
        raw-=1
    return str




if __name__ == '__main__':
    str='we are happy'
    str=list(str)
    print(len(str))
    # print(str.replace(' ','%20'))
    print(replace_str(str))