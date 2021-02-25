# 타이핑 게임 만들기

import time
import random

def getStringList(count):
    listData = []
    for i in range(1, count+1):
        listData.append("data {}".format(i))
    
    return listData

# print(getStringList(10))
WORD_LIST = getStringList(10)

random.shuffle(WORD_LIST)


