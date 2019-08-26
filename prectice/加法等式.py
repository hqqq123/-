for i in range(100,433):
    add1=i
    add2=532-i
    add1_k2=add1//10%10
    add1_k3=add1%10
    add2_k1=add2//100
    add2_k2=add2//10%10
    add2_k3=add2%10
    if(add1_k2==add2_k1 and add1_k3==add2_k2 and add2_k3==add2_k2):
        print(add1//100,add1_k2,add1_k3)