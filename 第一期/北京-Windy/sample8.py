#!/usr/bin/env  python
# -*- coding: UTF-8 -*-

<<<<<<< HEAD
class mul:
    '''实现x*y乘法表'''

    def __init__(self,cow,col):
=======
class Mul:
    '''实现x*y乘法表'''

    def __init__(self, cow, col):
>>>>>>> upstream/master
        self.cow = cow
        self.col = col

    def mul(self):
<<<<<<< HEAD
        self.col, self.cow=int(input())
        for i in
=======
        for self.cow in range(1, self.col):
            print(end='\n')
            for self.col in range(1, self.cow+1):
                print('%d*%d=%d' % (self.cow, self.col, self.cow*self.col), end='  ')


if __name__ == '__main__':

    m = Mul(int(input()), int(input()))
    m.mul()
>>>>>>> upstream/master
