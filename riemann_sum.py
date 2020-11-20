'''
Calculates Riemann Sums
@author: Zoe Bingham
'''
from math import *

def summation(graph="x", n=1, a=0, b=1, r_type = "left"):
    '''
    Returns the sum of n rectangles on the graph from the interval a to b. 
    Default is a left riemann sum of x with 1 rectangle on an interval [0,1]

    Parameters:
        graph(str)  :   the graph of an equation
        n(int)      :   the number of rectangles under the curve
        a(double)   :   beginning of interval
        b(double)   :   ending of interval
        r_type(str) :   right, left, or mid reimann sum
    
    Return
        r_sum(double):   the sum of the graph
    '''
    #init r_sum
    r_sum = 0
    #length of the interval
    interval = b-a
    #length of each rectangle's base
    partition = interval/n

    #left reimann sum
    if r_type.lower() == "left":
        for i in range(n):
            x = partition * i + a
            r_sum += eval(graph)*partition
    
    #right reimann sum
    if r_type.lower() == "right":
        for i in range(n):
            x = partition * (i+1) + a
            r_sum += eval(graph)*partition
    
    #mid reimann sum
    if r_type.lower() == "mid":
        for i in range(n):
            x = (partition/2) + a + (partition * i)
            r_sum += eval(graph)*partition

    return r_sum

def main():
    expression = input("Enter an expression to be summed: ")
    n = int(input("Enter the desired number of partitions: "))
    a = int(input("Enter the start of the interval: "))
    b = int(input("Enter the end of the interval: "))
    r_type = input("Enter the desired type of riemann sum: ")

    print(summation(expression, n, a, b, r_type))

if __name__ == "__main__":
    main()