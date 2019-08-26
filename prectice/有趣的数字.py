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
    od = OrderedDict()
    has_same_number = False
    min_abs_sub_pairs, max_abs_sub_pairs = 0, 0

    if n == 1:
        return "{}	{}".format(0, 0)
    for each_number in data:
        value = od.get(each_number, 0)
        if value > 0:
            has_same_number = True
        od[each_number] = value + 1
    if has_same_number:
        for each_number in od:
            min_abs_sub_pairs += od[each_number] * (od[each_number] - 1) // 2
    else:  # 无重复数字则依次遍历求取
        temp_od = od.copy()  # 拷贝一份以便后面处理
        pre_items = temp_od.popitem(last=False)  # 获取最小项
        min_abs_sub = -1  # 初始化
        #	遍历每一项
        for next_items in temp_od.items():
            if min_abs_sub == -1 or abs(pre_items[0] - next_items[0]) < min_abs_sub:
                min_abs_sub = abs(pre_items[0] - next_items[0])
                min_abs_sub_pairs = pre_items[1] * next_items[1]
            elif min_abs_sub == abs(pre_items[0] - next_items[0]):
                min_abs_sub_pairs += pre_items[1] * next_items[1]
            pre_items = next_items
    max_abs_sub_pairs = od.popitem(last=True)[1] * od.popitem(last=False)[1]
    return "{}	{}".format(min_abs_sub_pairs, max_abs_sub_pairs)


if __name__ == "__main__":
    while True:
        try:
            length = int(input())
            data = input()
            print(solve(length, data))
        except EOFError:
            break
