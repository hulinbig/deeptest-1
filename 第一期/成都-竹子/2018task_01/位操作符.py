# _*_coding:utf-8 _*_
#位操作符

'''位操作符只适用于整数,各种操作符均是通过计算机语言来计算的
1.~num   单目运算，对数的每一位取反。结果为-（num + 1）
2.num1 << num2 num1 左移 num2 位
3.num1 >> num2 num1 右移 num2 位
4.num1 & num2 num1 与 num2 按位 与
5.num1 ^ num2 num1 异或 num2
6.num1 | num2 num1 与 num2 按位 或
'''


def Binay(number):
    tmp = []
    result = ''
    while number:

        quyu = number % 2
        number = number // 2
        tmp.append(quyu)
    while tmp:
        # print(tmp)
        result += str(tmp.pop())

    return result

def Binay1(number):
    tmp = []
    result = ''
    while number:
        quyu = number % 2
        number = number // 2
        tmp.append(quyu)
    print(tmp)
    tmp = list(reversed(tmp))
    for i in tmp:
        result +=str(i)

    return result

def loh(a=30, b=60):
    c = a & b      #Binay1(a),Binay1(b)
    print("a&b的值为：", c)
    d = a | b
    print("a|b的值为：", d)
    e = a ^ b
    print("a ^ b的值为：", e)
    f = ~a
    print('~a的值为，', f)
    e = a << 2
    print('a << 2的值为', e)
    g = a >> 2
    print('a << 2的值为', g)


