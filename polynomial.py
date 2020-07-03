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

    def __add__(self, other):
        return [item1+item2 for (item1,item2) in zip(self.deg_lst, other.deg_lst)]

    def __sub__(self, other):
        return [item1-item2 for (item1,item2) in zip(self.deg_lst, other.deg_lst)]   

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
    p1 = poly(deg_lst)
    print(p1)
    print(poly(deg_lst))
    deg_lst2 = [1,1,1]
    p2 = poly(deg_lst2)
    print(p1 + p2)
    print(p1 - p2)
    print(np.dot(deg_lst,deg_lst2))

        
        