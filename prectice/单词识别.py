di={}
str=input()
str_list=str.replace(',',' ').lower().split('.')[0].split(' ')
for word in str_list:

    try:

        di[word]+=1
    except:
        di[word]=1
def sort(tup):
    return -tup[1],tup[0]
di=sorted(di.items(),key=sort)
# print(di)
for k,v in di:
    print(k,v)


