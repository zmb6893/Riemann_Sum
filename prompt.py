'''
Uses user input to graph a Riemann Sum
@author: Zoe Bingham
'''
from graph_sum import *

def check_quit(user_in):
    if user_in == "QUIT":
        quit()

def main():
    print("If at any time, you wish to exit the program, type QUIT")
    while True:
        try:
            expression = input("Enter an expression to be summed: ")
            check_quit(expression)
            n = (input("Enter the desired number of partitions: "))
            check_quit(n)
            a = (input("Enter the start of the interval: "))
            check_quit(a)
            b = (input("Enter the end of the interval: "))
            check_quit(b)
            r_type = input("Enter the desired type of riemann sum: ")
            check_quit(r_type)

        try:
            graph(expression, int(n), int(a), int(b), r_type)
        except:
            print("Make sure you have entered valid entries for each input")

if __name__ == "__main__":
    main()