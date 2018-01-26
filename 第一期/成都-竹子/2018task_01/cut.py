# _*_coding:utf-8 _*_
'''关于代码性能问题，循环里面不能每次进行判断或者判定的，
都统一用一个变量一次性判断后在进行接收'''
import string

def check_info9():
    alphas = string.ascii_letters + ''  #显示所有的字母包括大小写或新增允许输入的特殊字符
    nums = string.digits                #显示所有的数字
    alphasnums = alphas + nums
    yourinout = input('please input test')
    if len(yourinout) >= 1:
        if yourinout[0] not in alphas:
            print("invild: first must be Letter")
        else:
            for otherchar in yourinout[1:]:
                if otherchar not in alphasnums:
                    print("invild: other must be alphas or number")
                    break
    else:
        print('OKey,please once again')

check_info9()
