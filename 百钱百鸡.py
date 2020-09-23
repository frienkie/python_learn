for cock in range(1,101):   # 公鸡
    for hen in range(1,101):  #母鸡
        for chick in range(1,101): #小鸡
            if cock * 5 + hen * 3 + chick == 100:
                if cock + hen + chick * 3 == 100:
                    print(cock,hen,chick * 3)
