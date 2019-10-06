# coding: utf-8
get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
print("金鐘54")
msg=input("分類項目") 
if ("戲劇女主角" in msg):
    print ("得獎主:賈靜雯／我們與惡的距離")
elif ("戲劇男主角" in msg):
    print("得獎主:龍劭華【陳坤倉】／菜頭梗的滋味")
elif ("戲劇節目" in msg):
    print("得獎主:我們與惡的距離")
elif ("戲劇男配角" in msg):
    print("得獎主:溫昇豪／我們與惡的距離")
elif ("戲劇女配角" in msg):
    print("得獎主:曾沛慈／我們與惡的距離")
elif ("綜藝主持人" in msg):
    print("得獎主:黃子佼、卜學亮／超級同學會")
elif ("綜藝節目" in msg):
    print("得獎主:聲林之王")
elif ("電視電影" in msg):
    print("得獎主:你的孩子不是你的孩子 貓的孩子")
elif ("迷你劇集" in msg):
    print("得獎主:奇蹟的女兒")
elif ("節目創新" in msg):
    print("得獎主:台灣特有種")
elif ("終身成就" in msg):
    print("得獎主:張小燕")
else:
    print("請GOOGLE!!")
