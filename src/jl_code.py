import itertools

class Polynomial():

    def __init__(self, coeff_lst=None):
        self.coeff = coeff_lst
        self.result = 0
    
    def evaluate(self, x):
        for idx, val in enumerate(self.coeff):
            self.result += val*x**idx
    
    def derivative(self):
        diff_power = [0]
        new_coeff = [0]
        lst = []
        
        for i in range(1, len(self.coeff)):
            diff_power.append(i-1)
            new_coeff.append(self.coeff[i]*i)
        zipped = zip(reversed(new_coeff), reversed(diff_power))
        for val in zipped:
            lst.append(f'{val[0]}*x^{val[1]}')
        print('+'.join(lst))

    def integrate(self):
        int_power = []
        new_coeff = []
        lst = []
        
        for i in range(0, len(self.coeff)):
            int_power.append(i+1)
            new_coeff.append(i+1)
        zipped = zip(reversed(self.coeff), reversed(new_coeff), reversed(int_power))
        for val in zipped:
            lst.append(f'{val[0]}/{val[1]}*x^{val[2]}')
        print('+'.join(lst))
    
            
    def __repr__(self):
        return f'Polynomial({self.coeff})'
    
    def __add__(self, p):
        temp = Polynomial()
        temp.coeff = [x+y for x,y in itertools.zip_longest(self.coeff, p.coeff,
                                                           fillvalue=0)]
        return temp

    def __sub__(self, p):
        temp = Polynomial()
        temp.coeff = [x-y for x,y in itertools.zip_longest(self.coeff, p.coeff,
                                                           fillvalue=0)]          
        return temp

    def __neg__(self):
        coeffs = []
        for v in self.coeff:
            coeffs.append(-v)
        return Polynomial(coeffs)
    
    def __eq__(self, p):
        r1 = 0
        r2 = 0
        for idx, val in enumerate(self.coeff):
            r1 += 1*val**idx
            
        for idx, val in enumerate(p.coeff):
            r2 += 1*val**idx 
        return r1 == r2
    
    def __str__(self):
        len_lst = []
        for i in range(len(self.coeff)):
            len_lst.append(i)
        lst = zip(reversed(self.coeff), reversed(len_lst))
        out_lst = []
        for val in lst:
            out_lst.append(f'{val[0]}x^{val[1]}')
        out_str = '+'.join(out_lst)
        return out_str
    
    def __mul__(self, p):
        temp = Polynomial()
        temp.coeff = [x*y for x,y in itertools.zip_longest(self.coeff, p.coeff,
                                                           fillvalue=0)]
        return temp
                                                    


if __name__ == "__main__":
    
    p = Polynomial([3,2,1])
    p2 = Polynomial([1])
    p3 = p - p2
    # print(p3)
    p4 = -p
    # print(p==p2)
    # print(p)
    p3 = p*p2
    # print(p3)
    p.derivative()
    p.integrate()