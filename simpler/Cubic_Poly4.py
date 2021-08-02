# Exercise 9.2
from Line_Parabola import Parabola
'''
Note: I have handed in my version of the Line_Parabola.py program,
which is equal to the file from the book except that it contains an
if-test that makes sure the calls to classes in the program is not run
when the program is imported as a module.
I have also added print statements in the call methods from Line_Parabola.py,
which is reflected in the prints of this program.
'''

class Cubic(Parabola):
    def __init__(self, c0, c1, c2, c3):
        Parabola.__init__(self, c0, c1, c2)
        self.c3 = c3
        
    def __call__(self, x):
        print 'Cubic.__call__ called'
        return Parabola.__call__(self, x) + self.c3*x**3
        
    # table method is automatically imported from Line
    
class Poly4(Cubic):
    def __init__(self, c0, c1, c2, c3, c4):
        Cubic.__init__(self, c0, c1, c2, c3)
        self.c4 = c4
        
    def __call__(self, x):
        print 'Poly4.__call__ called'
        return Cubic.__call__(self, x) + self.c4*x**4
        
    # table method is automatically imported from Line
    
cub = Cubic(1, 2, 3, 4)
print cub(2)    # expect 1 + 2*2 + 3*4 + 4*8 = 49
pol4 = Poly4(5, 4, 3, 2, 1)
print pol4(3)   # expect 5 + 4*3 + 3*9 + 2*27 + 1*81 = 179

'''
Terminal>python Cubic_Poly4.py 
Cubic.__call__ called
Parabola.__call__ called
Line.__call__ called
49
Poly4.__call__ called
Cubic.__call__ called
Parabola.__call__ called
Line.__call__ called
179
'''
