import re
def int_num(a):
    while True:
        n=input(str(a))
        try:
            if type(int(n))==int:
                break
        except Exception as e:
            print("please enter int only")
    return int(n)