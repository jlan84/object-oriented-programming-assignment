import numpy as np
import math

class poly(object):
    def __init__(self, deg_lst):
        self.power_list = []
        self.deg_lst = deg_lst
        for i in range(len(self.deg_lst)):
            self.power_list.append(i)
    
    def eval_poly(self, x):
        sum = 0
        for i in range(len(self.deg_lst)):
            sum += self.deg_lst[i]*x**self.power_list[i]
        return sum

    def two_polys(self, deg2_lst):
        pass

    def __repr__(self):
        return f'Polynomial {self.deg_lst}'


    def __str__(self):
        poly_string = ''
        for i in range(len(self.deg_lst)-1,-1,-1):
            if i==0:
                poly_string += f'{self.deg_lst[i]} '
            else:
                poly_string+= f'{self.deg_lst[i]}x^{self.power_list[i]}+'
        return poly_string







if __name__ == '__main__':
    deg_lst = [3,2,1]
    p1 = poly(deg_lst).eval_poly(2)
    print(p1)
    print(poly(deg_lst))



        
        