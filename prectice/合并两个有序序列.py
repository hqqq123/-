def merge_loop(list1,list2):
    list3=list()
    while list1 and list2:
        if list1[0]<list2[0]:
            list3.append(list1[0])
            del list1[0]
        else:
            list3.append(list2[0])
            del list2[0]
    list3.extend(list1)
    list3.extend(list2)
    return list3
def merge_digui(list1,list2):
    list3=list()
    def merge(list1,list2,list3):
        if len(list1)==0 or len(list2)==0:
            list3.extend(list1)
            list3.extend(list2)
            return list3
        elif list1[0]<list2[0]:
            list3.append(list1[0])
            del list1[0]

        elif list1[0]>=list2[0]:
            list3.append(list2[0])
            del list2[0]
        return merge(list1,list2,list3)
    return merge(list1,list2,list3)
if __name__ == '__main__':
    list1=[1,2,3]
    list2=[1,1,2,5]
    # list3=merge_loop(list1,list2)
    list3=merge_digui(list1,list2)
    print(list3)