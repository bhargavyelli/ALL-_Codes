def question1(l):
    print(l[1])
    for i in range(len(l)):
        if l[i] == "banana":
            l[i] = "kiwi"
    print(l)
    print("length of the list is : ", len(l))

def question4(l):
    l2 = [i for i in l if i.find('a') != -1]
    print(l2)
    l3 = [i.upper() for i in l]
    print(l3)
    l4 = ["kiwi" if i == "banana" else i for i in l]
    print(l4)
def question7(l):
    print("number of greens in the list is :",l.count("green"))
    print("Index of blue is :",l.index("blue"))
    l.reverse()
    print("After reversing the list :",l)
    print("After clearing the list :",l.clear())
def question12(l):
    l1=[]
    for i in l:
        for j in i:
            l1.append(j)
    print(l1)
# question1(["apple", "banana", "cherry"])
# question4(["apple", "banana", "cherry", "kiwi", "mango"])
question7(["red", "green", "blue", "green","red", "green", "blue", "green"])
# question12([[1, 2], [3, 4], [5, 6]])