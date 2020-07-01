import numpy as np
import math

class Poly(object):
    def __init__(self, deg_lst):
        self.power_list = []
        self.deg_lst = deg_lst
        for i in range(len(self.deg_lst)):
            self.power_list.append(i)
    
    def eval_poly(self, x):
        sum_ = 0
        for i in range(len(self.deg_lst)):
            sum_ += self.deg_lst[i]*x**self.power_list[i]
        return sum_

    def __add__(self, other):
        return Poly([item1+item2 for (item1,item2) in zip(self.deg_lst, other.deg_lst)])

    def __sub__(self, other):
        return Poly([item1-item2 for (item1,item2) in zip(self.deg_lst, other.deg_lst)])

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

    def __mul__(self,other):
        self_arr1 = np.array(self.deg_lst)
        other_arr1 = np.array(other.deg_lst)
        return Poly(np.polymul(self_arr1,other_arr1))

    def derivative(self):
        arr = np.array(self.deg_lst)
        return Poly(np.polyder(arr))

    def integral(self):
        rev_arr = self.deg_lst
        arr = np.array(rev_arr)
        return Poly(np.polyint(arr)[::-1])

    def __eq__(self, other):
        return self.deg_list == other.deg_list

    




if __name__ == '__main__':
    deg_lst = [1,2,3]
    p1 = Poly(deg_lst)
    # print(p1)
    # print(Poly(deg_lst))
    deg_lst2 = [1,2]
    p2 = Poly(deg_lst2)
    # print(p1 + p2)
    # print(p1 - p2)
    print(p1*p2)


        
        