def question1():
    a = b = 10
    b = 20
    print(a,b)
def question4():
    x = [1,2,3]
    y=x
    x[0] = 9
    print(x,y)
def question5():
    print(3 == 3.00)
    print(3 is 3.0)
def question6():
    a = (5)
    b = (5,)
    print(type(a))
    print(type(b))
def question10():
    a = "5"
    b = 5
    c = a * b
    d = b * a
    print(c, d)
def question16():
    x = 1000
    y = 1000
    print(x is y)
def question20():
    x = 10
    print(type(x))
    x = 3.14
    print(type(x))
    x = "str"
    print(type(x))

question1()
question4()
question5()
question6()
question10()
question16()
question20()
