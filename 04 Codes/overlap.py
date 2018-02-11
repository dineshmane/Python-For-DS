print("heelo")
import sys
if sys.argv[1]=="" or sys.argv[2]=="" :
    print("please enter the file name")
else:
    print("all okie")
    f1 = open(sys.argv[1],"r")
    f2 = open(sys.argv[2],"r")
    list1 = []
    list2 = []
    for i in f1.readlines():
        list1.append(int(i))
    for i in f2.readlines():
        list2.append(int(i))

    s1 = set(list1)
    s2 = set(list2)
    s1.intersection(s2)
    print(s1.intersection(s2))