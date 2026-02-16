def fun1(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end  = " ")
        print()

def fun2(n):
    for i in range(n):
        for j in range(n):
            if i==0 or j==0 or i == n-1 or j==n-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

def fun3(n):
    for i in range(n):
        for j in range(n):
            if(j<n-i-1):
                print(" ",end=" ")
            else:
                print("*",end=" ")
        print()

def fun4(n):
    for i in range(n):
        if(i <= n/2):
            for j in range(i+1):
                print("*",end=" ")
        if(i>n/2):
            for j in range(n-i):
                print("*",end=" ")

        print(" ")


n = int(input("Enter a number"))
fun1(n)
print("==============")
fun2(n)
print("==============")
fun3(n)
print("==============")
fun4(n)