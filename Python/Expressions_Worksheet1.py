def question1():
    print(7*7)

def question2():
    a,b,c,x = 2,3,4,5
    print(a*x*x + b*x + c)

def question3():
    print(29 % 6)

def question4(num):
    print("Positive" if num>0 else "Negative" if num<0 else "Zero")

def question5():
    n = -12
    print(abs(n))

def question6():
    a,b = 15,8
    a,b = b,a
    print(a,b)

def question7(x,y,z):
    print((x+y+z)/3)

def question8(a,b):
    print(a if a<b else b)

def question9():
    x,y = 9,5
    print(x|y, x^y)

def question10():
    num = 18
    print(num%2==0 and num%3==0)

def question11():
    a,b,c = 14,27,19
    print(a*(a>=b)*(a>=c) + b*(b>=a)*(b>=c) + c*(c>=a)*(c>=b))

def question12():
    n = 32
    print(n>0 and (n & (n-1))==0)

def question13():
    a,b,c = 20,12,18
    print(a+b+c - (a*(a>=b)*(a>=c) + b*(b>=a)*(b>=c) + c*(c>=a)*(c>=b))
          - (a*(a<=b)*(a<=c) + b*(b<=a)*(b<=c) + c*(c<=a)*(c<=b)))

def question14():
    n,bit = 12,2
    print(n ^ (1<<bit))

def question15():
    n = 29
    print(bin(n).count('1'))

def question16():
    n = -56
    print((n>0) - (n<0))

def question17():
    n = 12
    print(n%4==0 and n%8!=0)

def question18():
    n,k = 150,2
    print(((n<<k)|(n>>(8-k))) & 0xFF)

def question19():
    a,b,c = 8,27,14
    print((a*(a>=b)*(a>=c) + b*(b>=a)*(b>=c) + c*(c>=a)*(c>=b))
          - (a*(a<=b)*(a<=c) + b*(b<=a)*(b<=c) + c*(c<=a)*(c<=b)))

def question20():
    n,bit = 9,3
    print(n | (1<<bit))


question1()
question2()
question3()
question4(-8)
question5()
question6()
question7(5,8,10)
question8(20,13)
question9()
question10()
question11()
question12()
question13()
question14()
question15()
question16()
question17()
question18()
question19()
question20()
