#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 21:33:47 2019

@author: singg
"""

def gred_descent(f,df,start,iterations,n):
    x_current = start
    y_current = f(x_current)
    y_new = y_current
    for i in range(1,iterations):
        y_new = f(x_current) - n * df(x_current)
        
        if y_new < y_current:
            x_current = x_current - n
        else:
            x_current = x_current + n
        y_current = y_new
    return (x_current, y_new)
    
def square(x):
    return x*x

if __name__ == '__main__':
    # Lets say we have a function f(x) = x*x. And we want to minimize
    # its value. 
    print(gred_descent(lambda x:x*x,lambda x:2*x,4,1000, 0.01))
    print(gred_descent(lambda x:x*x-5*x+6 ,lambda x:2*x-5,4,1000, 0.01))
    print(gred_descent(lambda x:x*x*x+2*x-3 ,lambda x:3*x*x+2,4,10000, 0.01))