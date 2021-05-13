'''https://drive.google.com/file/d/1B-OQWSRFdahYzos0QCJV6rfskiK0nrxt/view?usp=sharing'''

a = int(input("введите a "))
b = int(input("введите b "))
c = int(input("введите c "))

if (a > b):
    if(a > c):
        if(b > c):
            print(b)
        else:
            print(c)
    else:
        print(a)
else:
    if(b > c):
        if(a > c):
            print(a)
        else:
            print(c)
    else:
        print(b)