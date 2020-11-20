"""
Graphs a mathematical expression with it's riemman sums
@author: Zoe Bingham
"""
import riemann_sum as rs
import matplotlib.pyplot as p
import matplotlib.patches as pa
import numpy as n
from math import *

def init_graph(expression, r_type, summed):
    '''
    Initializes graph's titles

    Parameters:
    expression (string): the expression that goes in the title of the graph
    r_type (string):     the type of Riemann Sum
    summed (string):     the sum of the rectangles under the curve
    '''
    title = "Riemann Sum (" + r_type + ") of the Graph: " + expression + '=' + summed
    p.title(title)
    p.xlabel("x")
    p.ylabel("y")

def f(x, expression):
    '''
    Evaluates the expression at x

    Parameters:
    expression (string):    the expression to be evaluated
    x (float):              the point at which the expression will be evaluated at
    '''
    return eval(expression)

def graph_curve(expression, a, b, accuracy):
    '''
    Graph's the curve.

    Parameters:
    expression (string):    the expression to be graphed
    a (float):              the starting point
    b (float):              the ending point
    accuracy (int):         the number of points in the interval
    '''
    x = n.linspace(a, b, accuracy)
    y = n.zeros(len(x))
    for i in range(len(x)):
        y[i] = f(x[i], expression)

    p.plot(x, y, 'k')
    p.show()

def graph_rectangles(graph="x", n=1, a=0, b=1, r_type = "left"):
    '''
    Graph's the rectangles under the curve.

    Parameters:
        graph(str)  :   the graph of an equation
        n(int)      :   the number of rectangles under the curve
        a(double)   :   beginning of interval
        b(double)   :   ending of interval
        r_type(str) :   right, left, or mid reimann sum
    '''
    #length of the interval
    interval = b-a

    #length of each rectangle's base
    partition = interval/n

    # Create figure and axes
    fig, ax = p.subplots(1)

    #left reimann sum
    if r_type.lower() == "left":
        for i in range(n):
            x = partition * i + a
            y = eval(graph)
            rect = pa.Rectangle((x,0),partition,y, linewidth = 1, edgecolor="k", facecolor="b")
            ax.add_patch(rect)
    
    #right reimann sum
    if r_type.lower() == "right":
        for i in range(n):
            x = partition * (i+1) + a
            y = eval(graph)
            rect = pa.Rectangle((x-partition,0),partition,y, linewidth = 1, edgecolor="k", facecolor="r")
            ax.add_patch(rect)
    
    #mid reimann sum
    if r_type.lower() == "mid":
        for i in range(n):
            x = (partition/2) + a + (partition * i)
            y = eval(graph)
            rect = pa.Rectangle((x-(partition/2),0),partition,y, linewidth = 1, edgecolor="k", facecolor="g")
            ax.add_patch(rect)

def graph(expression, n, a, b, r_type, accuracy = 50):
    '''
    Graphs the expression from a to b with labelled graph.

    Parameters:
    expression(string): used in title and to graph the curve
    n(int):             the number of rectangles under the curve
    a (float):          beginning of the interval
    b (float):          end of the interval
    r_type(str):        right, left, or mid reimann sum
    accuracy (int):     the accuracy of the graph
    '''
    #gets the sum of the rectangles under the curve
    summed = str(rs.summation(expression, n, a, b, r_type))

    #graphs the expression and the rectangles
    graph_rectangles(expression, n, a, b, r_type)
    init_graph(expression, r_type, summed)
    graph_curve(expression, a, b, accuracy)

    #displays the graph
    p.show()
