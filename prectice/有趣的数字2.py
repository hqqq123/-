#
# def solve(n,data):
#     data=sorted(set(map(int,data.split())))
#     print(data,type(data))
#
# # n=input()
# # data=input()
# solve(4,'45 2 45 6')

from collections import OrderedDict

__author__ = '__L1n__w@tch'


def solve(n, data):
    data = sorted(list(map(int, data.split())))
    #	读取时创建字典,	判断是否有重复数字
    od = {}
    has_same_number = False
    min_abs_sub_pairs, max_abs_sub_pairs = 0, 0
    length=0
    if n == 1:
        return "{}	{}".format(0, 0)
    for each_number in data:
        length+=1
        value = od.get(each_number, 0)
        if value > 0:
            length-=1
            has_same_number = True
        od[each_number] = value + 1
    if has_same_number:
        i=0
        for each_number in od:
            min_abs_sub_pairs += od[each_number] * (od[each_number] - 1) // 2
            if i==0:
                min_count=od[each_number]
            if i==length-1:
                max_count=od[each_number]
            i+=1
        max_abs_sub_pairs=min_count*max_count
    else:  # 无重复数字则依次遍历求取
        i=n-1
        min=11111
        count=1
        print(data)
        while i>0:
            cha=data[i]-data[i-1]
            if cha==min:
                count+=1
                print(cha)
            if cha<min:
                min=cha
                count=1

            i-=1
        max_abs_sub_pairs = 1
        min_abs_sub_pairs=count
    return "{}	{}".format(min_abs_sub_pairs, max_abs_sub_pairs)


if __name__ == "__main__":
    while True:
        try:
            length = int(input())
            data = input()
            print(solve(length, data))
        except EOFError:
            break
