import sys
if sys.argv[1]=="" :
    print("please enter the file name")
else:
    try:
        f1 = open(sys.argv[1],"r")
        list1 = []
        for i in f1.readlines():
            list1.append(i.strip())

        for i in sys.argv[2:] :
            print(list1[int(i)-1])
    except FileNotFoundError as e:
        print("Make sure the file name: ",e)
    except ValueError as e:
        print("kuch toh gadbad hai daya", e)

