def coin_change(values,money):

    coins=[0 for i in range(money+1)]
    for i in range(1,money+1):
        min_coins=i
        for value in values:
            if value<=i:
                temp=coins[i-value]+1
                if temp<min_coins:
                    min_coins=temp
        coins[i]=min_coins
        print('面值为%s的最小硬币数为：%s' %(i,coins[i]))


if __name__ == '__main__':
    values=[1,2,5,10]
    money=23
    coin_change(values,money)