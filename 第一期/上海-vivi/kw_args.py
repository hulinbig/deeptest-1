# -.- coding:utf-8 -.-#关键字参数；可以传入0个或任意个参数名的参数，这些关健字参数在函数内部自动组装为一个dict'''def print_scores(**kw):    print('      Name  Score')    print('----------------------')    for name, score in kw.items():        print('%10s  %d' % (name, score))      # %10s表字符串里含有10个占位符    print()print_scores(Adam=99, Lisa=88, Bart=77)data = {    'Adam Lee': 99,    'Lisa S': 88,    'F.Bart': 77}print_scores(**data)'''#命名关键字参数：与关键字不同的是，这里需要一个特殊分隔符，*后面的参数被视为命名关健字参数，调用的时候一定要传入参数名，否则报错'''def print_info(name, * , gender, city='beijing'):    print('Personal  Info')    print('--------------')    print('    Name: %s' % name)    print('    Gender: %s' % gender)    print('    City: %s'% city)    print('    Age: %s' % age)    print()print_info('Bob', gender='male', age=20)     #执行结果显示报错，*后无这个关键字参数print_info('Lisa', gender='female', city='shanghai')'''#参数组合def f1(a,b,c=0, *args, **kw):    print('a=', a, 'b= ', b, 'c=', c, 'args=', args, 'kw=', kw)def f2(a, b, c=0, *, d, **kw):    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)f1(1, 2)f1(1, 2, 3)f1(1, 2, 3, 'a', 'b')f1(1, 2, 3, 'a', 'b', x=99)#执行结果为# a= 1 b=  2 c= 0 args= () kw= {}# a= 1 b=  2 c= 3 args= () kw= {}# a= 1 b=  2 c= 3 args= ('a', 'b') kw= {}# a= 1 b=  2 c= 3 args= ('a', 'b') kw= {'x': 99}f2(1, 2, d=99, ext=None)#执行结果为a= 1 b= 2 c= 0 d= 99 kw= {'ext': None}args = (1, 2, 3, 4)kw = {'d': 99, 'x': '#'}f1(*args, **kw)#执行结果为a= 1 b=  2 c= 3 args= (4,) kw= {'d': 99, 'x': '#'}args = (1, 2, 3)kw = {'d': 99, 'x': '#'}f2(*args, **kw)#执行结果为a= 1 b= 2 c= 3 d= 99 kw= {'x': '#'}