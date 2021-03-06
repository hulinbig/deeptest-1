'''
Created on 2018年1月9日

@author: 早安阳光
'''
class Calc:
    # 初始化
    def __init__(self,a,b):
        self.a = a
        self.b = b
    # 加法
    def __add__(self):
        if type(self.a) != int or type(self.b) != int:
            raise Exception("a、b必须为int型")
        return self.a+self.b
    # 减法
    def __sub__(self):
        if type(self.a) != int or type(self.b) != int:
            raise Exception("a、b必须为int型")
        return self.a-self.b
    # 乘法
    def __mul__(self):
        if type(self.a) != int or type(self.b) != int:
            raise Exception("a、b必须为int型")
        return self.a*self.b
    # 除法
    def __div__(self):
        if type(self.a) != int or type(self.b) != int:
            raise Exception("参数必须为int型!")
        if self.b == 0:
            raise Exception("除数不能为0！",self.b)
        return self.a/self.b
#使用示例
print(Calc(66,88).__add__())
print(Calc(88,66).__sub__())
print(Calc(6,8).__mul__())
print(Calc(88,2).__div__())