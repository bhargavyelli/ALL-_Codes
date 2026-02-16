def question1(a,b):
    print("sum, difference, product, and quotient of {} and {} is: ".format(a,b),end=" ")
    print(a+b, " ", a-b, " ", a*b, " ", a/b)

def question2(a,b):
    print("after adding 2 float numbers rounded to 2 decimal points {:.2f}".format(a+b))

def question3(s1,s2):
    s3 = s1+" "+s2
    print("After concatenating 2 strings: ",s3)

def question4(s1):
    print(s1*5)

def question5(a,b):
    print("comparison {} and {} is: ".format(a,b),end=" ")
    print(a==b, " ", a!=b, " ", a<b, " ", a>b, " ",a>=b, " ", a<=b)

def question6(a,b,s1,boo):
    print(a," - ",type(a))
    print(b," - ",type(b))
    print(s1," - ",type(s1))
    print(boo," - ",type(boo))

def question7(s1):
    print("After converting string to int and float: ",int(s1)," ",float(s1))
    print("Types: ", type(int(s1)), type(float(s1)))

def question8(a,s1):
    print("After adding int and str after converting explicitly: ",a+int(s1))

def question9(a,b):
    csum = a+b
    cdiff = a-b
    cprod = a*b
    print("Sum: {}, Difference: {}, Product: {}".format(csum, cdiff, cprod))

def question10(a,b):
    print("Quotient: {}, Remainder: {}".format(a//b, a%b))

def question11():
    s1,f,b = "Python",3.14,True
    print(s1," ",f," ",b)

def question12(s1,s2):
    print("Before Swapping: s1 = {}, s2 = {}".format(s1,s2))
    s1,s2 = s2,s1
    print("After Swapping: s1 = {}, s2 = {}".format(s1,s2))

def question13():
    a = 10
    print(a,type(a))
    a = 3.14
    print(a,type(a))
    a = "Python"
    print(a,type(a))

def question14(r):
    pi = 3.14159
    print("Circumference of a circle having radius {} is: {:.2f}".format(r,pi*r*2))

def question15(name, age, favnum):
    print(f"My name is {name}, age is {age}, and my favorite number is {favnum}.")

def question16(a,b):
    print("Quotient = {}, Remainder = {}".format(a//b, a%b))

def question17():
    x = 10
    x += 5
    print(x)
    x -= 3
    print(x)
    x *= 2
    print(x)
    x /= 4
    print(x)

def question18():
    print("Python\'s \"syntax\" is easy")

def question19():
    print(True+True, True*False)

def question20():
    try:
        print(5+"Hello")
    except TypeError as e:
        print("Error:", e)

def question21():
    a = 1234567890987654321
    print(a," ",type(a))

def question22():
    a = b = c = 100
    print(a,b,c)

def question23(a):
    print(a)
    print(type(a))

def question24():
    a = 10
    b = 3.5
    print(a+b, type(a+b))

def question25():
    s = "PythonProgramming"
    print(s[:6], s[6:])


question1(7,4)
question2(5.2345,8.6543)
question3("hello","world")
question4("Hello")
question5(4,5)
question6(2,3.43,"hello",True)
question7("50")
question8(25,"25")
question11()
question12(18,487)
question13()
question14(5)
question15("Alice", 20, 7)
question16(17,5)
question17()
question18()
question19()
question20()
question21()
question22()
question23(None)
question24()
question25()
