# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 15:07:57 2020

@author: Administrator
"""
count = 0
def hanoi(n,src,dst,mid):
    global count
    if n == 1:
        print('{}:{}->{}'.format(1,src,dst))
        count +=1
    else:
        hanoi(n-1,src,mid,dst)
        print('{}:{}->{}'.format(n,src,dst))
        count +=1
        hanoi(n-1,mid,dst,src)
hanoi(3,'左','右','中')
print(count)