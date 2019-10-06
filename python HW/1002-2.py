# coding: utf-8
from numpy.random import randint
words='''
我
我的
你
你的
心
溫柔
日子
雨
天空
等待
哭泣
忘記
分離
戀愛
思念
吹過
心醉'''
n=randint(3,6)

for i in range(n):
    k=randint(5,8)
    egg=choice(phrase,k)
    ham=''.join(egg)
    print(ham)
