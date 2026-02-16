from itertools import permutations


def question3(n):
    l = n.split(" ")
    l = l[::-1]
    n = ""
    for i in l:
        n = n+i+" "
    print(n)
def question7(n):
    d = {}
    for i in n:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
    mini = min(d.values())
    l = [k for (k,v) in d.items() if v == mini]
    print(l)
def question6(n):
    d = {}
    for i in n:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
    n = ""
    for k in d.keys():
        n += k
    print(n)

def question13(s1,s2):
    l = s1.split(" ") + s2.split(" ")
    d = {}
    for i in l:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    result = [key for key,value in d.items() if value == 1]
    print(result)

def question14(s):
    s.replace(',','#')
    s.replace('.',',')
    s.replace('#','.')
    print(s)
    
def question15(s):
    perm = permutations(s)
    n=""
    for p in perm:
        print("".join(p))
    
def question20(s):
    l = [i for i in s]
    print(l)
def question22(s):
    s.sort()
    print(s)
def question23(s):
    d =set()
    for i in s:
        d.add(i)
    print(d)

# question6("programming")
# question7("statistics")
# question3("This is Python")
# question13("red blue green", "blue yellow red")
# question14("23,45.89,78.90")
# question15("abc")
# question20("abc")
# question22(["pear", "apple", "banana"])
question23("balloon")


