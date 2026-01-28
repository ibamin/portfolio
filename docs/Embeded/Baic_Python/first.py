# -*- coding: utf-8 -*-
# print("hello world")


def add(a, b):
    answer = a + b
    return answer


# integer
def integer_test():
    a = 123
    print(type(a))
    a = 100 * 100
    print(a)
    a, b = 9, 2
    print(a * b)


# string
def string_test():
    a = "python chears"
    print(a)
    print(type(a))
    b = "python go"
    print(type(b))
    print(b)


# split
def split_test():
    a = "a:b:c:d"
    b = a.split(":")
    print(b)

    c = "#".join(b)
    print(c)

    a = "000-1111-2222"
    b = a.split("-")
    print(b)

    a = "1234567-1234567"
    b = a.split("-")
    print(b)


# list
def list_test():
    my_list = []
    print(my_list)
    my_list = [1, 2, 3, 4, 5]
    print(my_list)
    my_list = ["A string", 23, 100.32, "o"]
    print(my_list)
    my_list = [x + 100 for x in range(1, 11)]
    print(my_list)

    a, b, c, d = 0, 0, 0, 0
    hap = 0
    a = int(input("1st :"))
    b = int(input("2nd :"))
    c = int(input("3rd :"))
    d = int(input("4th :"))
    hap = a + b + c + d
    print("hap :%d" % hap)

    my_list = []
    hap = 0
    my_list.append(int(input("1st :")))
    my_list.append(int(input("2nd :")))
    my_list.append(int(input("3rd :")))
    my_list.append(int(input("4th :")))
    hap = sum(my_list, 0)
    print("hap :%d" % hap)


# range
def range_test():
    aa = []
    aa.append(100)
    aa.append(200)
    aa.append(300)
    aa.append(400)

    print("리스트변수 크기는 %d" % len(aa))
    print(aa)
    bb = []
    for i in range(0, 100):
        bb.append(i)
    print(bb)


# list slicing
def list_slicing_test():
    aa = [10, 20, 30, 40]
    print("aa[-1]은 %d, aa[-2]는 %d" % (aa[-1], aa[-2]))
    print(aa[0:2])
    print(aa[2:4])
    print(aa[0:])

    my_list = [0, 1, 2, 3, 4, 5]
    print(id(my_list))

    my_list[1:3] = ["A", "B", "C"]
    print(id(my_list))

    print(my_list)

    my_list = [0, 1, 2, 3, 4, 5]
    print(id(my_list))

    my_list[1:5] = ["A", "B"]
    print(id(my_list))

    print(my_list)


# function in list
def function_in_list():
    aa = [30, 10, 20]
    print("now list status :%s" % aa)
    aa.append(40)
    print("after append :%s" % aa)
    aa.pop()
    print("after pop :%s" % aa)
    aa.sort()
    print("after sort :%s" % aa)
    aa.reverse()
    print("after reverse :%s" % aa)
    aa.insert(2, 222)
    print("after insert :%s" % aa)
    print("index of value 20 :%d" % aa.index(20))
    aa.remove(222)
    print("after remove value 222 :%s" % aa)
    aa.extend([77, 88, 77])
    print("after extend list [77,88,77] :%s" % aa)
    print("counting value 77 :%d" % aa.count(77))


# list sorting str
def list_sorting_str():
    my_list = [
        "Computer",
        "Program",
        "Hardware",
        "Software",
        "Operating System",
        "Processor (CPU)",
        "Memory",
        "RAM (Random Access Memory)",
        "ROM (Read-Only Memory)",
        "Storage Devices",
        "Network",
        "Internet",
        "Browser",
        "Website",
        "Server",
        "Client",
        "Database",
        "Algorithm",
        "Programming Language",
        "Variable",
        "Conditional Statement",
        "Loop",
        "Function",
        "Class",
        "Object",
        "Compiler",
        "Debugging",
        "Interface",
        "GUI (Graphical User Interface)",
        "API (Application Programming Interface)",
        "Platform",
        "Cloud Computing",
        "Security",
        "Encryption",
        "Big Data",
        "Virtualization",
        "Artificial Intelligence",
        "Machine Learning",
        "Deep Learning",
        "Agile Development",
        "Version Control",
        "IoT (Internet of Things)",
        "API (Application Programming Interface)",
        "Mobile App",
        "Web App",
        "App Store",
        "User Interface (UI)",
        "User Experience (UX)",
        "Firewall",
        "Malware",
    ]
    my_list.sort(reverse=True)
    print("sorting my_list :%s" % my_list)


def gap_of_extend_plus():
    a = [1, 2, 3]
    print(id(a))

    a = a + [4, 5]
    print(id(a))
    print(a)

    b = [1, 2, 3]
    print(id(b))
    b.extend([4, 5])
    print(id(b))


# multi dimension list
def multi_dimension_list():
    aa = [[1, 2, 3, 4], [5, 67, 8], [9, 19, 11, 12]]
    print(aa[0])
    print(aa[0][0])
    print(aa[1][2])


# tuple
def tuple_test():
    str = "string of python"
    print(str[0])
    print(str[-1])

    card = "red", 4, "python"
    print(card)
    print(card[1])

    # 언팩킹
    a, b, c, _ = card
    print(a)
    print(b)
    print(c)
    d = False
    print(d)


def tuple_test():
    my_tuple = (1, 2, 3)
    print(my_tuple.index(1))

    str_tuple = ("베계", "이불", "침대")
    print(str_tuple.index("이불"))


def set_test():
    s = {100, 55, 1, 1, 1, 1, 2, 3}
    print(s)

    k = {5, 6, 7}
    k.add(1)
    print(k)

    # when create empty set do not s={} because that's make dictionary

    a = {0, 2, 4, 6, 8}
    b = {1, 2, 3, 4, 5}

    print("union :", a | b)
    print("intersection :", a & b)
    print("Difference :", a - b)
    print("Symmetric difference set :", a ^ b)


def dictionary_test():
    d = {}
    d = dict()
    d = {
        "banana": "single leaf plant",
        "iron man": "just iron man",
        123: 456,
    }
    print(d)

    d1 = {"one": 1, "two": 2, "tree": 3}
    print(d1)
    d2 = dict({"three": 3, "one": 1, "two": 2})
    print(d2)
    d3 = dict({"one": 1, "three": 3, "two": 2})
    print(d3)
    d4 = dict(one=1, two=2, three=3)
    print(d4)

    d5 = dict({("two", 2), ("one", 1), ("three", 3)})
    print(d5)
    d6 = dict(zip(["one", "two", "three"], [1, 2, 3]))
    print(d6)

    d = {"captain": "captain", "captain": "America"}
    print(d)

    d = {"A": 65, "B": 66, "C": 67}
    print(d["B"])

    d = {"Number": 10, "Name": "Konan", "Age": 23, "Home": "Seoul"}
    print(d)

    print(d["Age"])

    d["Age"] = 24
    print(d["Age"])

    d["Job"] = "Detective"
    print(d)

    print(d.keys())
    print(d.values())

    print("Home" in d)
    del d["Home"]
    print("Home" in d)

    print(d)


def dictionary_test2():
    my_list = [1, 2, 3, 4, 5]
    del my_list[0:6:2]  # index 0,2,4 즉 1,3,5삭제
    print(my_list)

    a = {"A": 90, "B": 80}
    print(a["A"])
    print(a["B"])

    print(a.get("C"))


def while_test():
    A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
    sum = 0
    while A:
        t = A.pop()
        if t >= 50:
            sum += t

    print(sum)


def split_test2():
    user_input = "65,45,2,3,45,8"
    sum = 0
    i = user_input.split(",")
    for a in i:
        sum += int(a)

    print(sum)


def GuGuDan():
    dan = int(input("GuGuDan Dan Number :"))
    if dan < 2 or dan > 9:
        print("Wrong Input data")
        exit()
    for i in range(1, 10):
        print(dan * i, end=" ")


def function1():
    print("This print about function1")


def function2(str="This print about function2"):
    print(str)


def function_test():
    function1()
    function2()
    function2("i want go home plz")


def mydef1():
    i = 10
    j = 20
    print(i + j)


def mydef2(i, j):
    print(i + j)


def mydef3(i, j, p):
    if p == "+":
        print(i + j)
    elif p == "-":
        print(i - j)
    elif p == "*":
        print(i * j)
    elif p == "/":
        print(i / j)


def mydef_test():
    mydef1()
    mydef2(10, 20)

    i = int(input("1st Number ."))
    j = int(input("2nd Number ."))
    p = input("operator :")
    mydef3(i, j, p)


def draw_pyramid(num_lines):
    for j in range(1, num_lines + 1):
        for i in range(num_lines - j):
            print(" ", end="")
        for i in range(j * 2 - 1):
            print("*", end="")
        print()


def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n - 2) + fibo(n - 1)


def ofstream():
    fruits = []
    fruits.append("Guava")
    fruits.append("Durian")
    fruits.append("Strawberry")
    fruits.append("PineBerry")
    fruits.append("Lime")

    f = open("C:/MyMoble/python/Ch01/test.txt", "w")
    for fruit in fruits:
        f.write(fruit)
        f.write("\n")
    f.close()


def ifstream():
    f = open("C:/MyMoble/python/Ch01/test.txt", "r")
    fruits = []
    line = f.readline()
    while line:
        fruits.append(line.strip())
        line = f.readline()
    f.close()
    print(fruits)


def lines_check(line):
    for i in range(0, len(line)):
        if line[i] < "0" or line[i] > "9":
            return True
    return False


def average_on_file():
    f = open("C:/MyMoble/python/Ch01/sample.txt", "r")
    line = "dumptext"
    cnt = 0
    sum = 0
    while 1:
        line = f.readline()
        line = line.strip()
        if lines_check(line):
            tmp = line.split(":")
            line = tmp[1]
        if line == "":
            break
        cnt += 1
        sum += float(line)
    f.close()

    f = open("C:/MyMoble/python/Ch01/sample.txt", "a")
    f.write("Average:")
    f.write(str(sum / cnt))
    f.write("\n")
    f.close()


import time

filename = time.strftime("%Y%m%d_%H%M%S")
print(filename)

fruits = []
fruits.append("Guava")
fruits.append("Durian")
fruits.append("Strawberry")
fruits.append("PineBerry")
fruits.append("Lime")
f = open(filename + ".txt", "a+")
for fruit in fruits:
    f.write(fruit)
    f.write("\n")
f.close()
