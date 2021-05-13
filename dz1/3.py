'''https://drive.google.com/file/d/1h9dPF5WxoYhLIXwX0H9jq8FC3qkP9xRf/view?usp=sharing'''

a = (input("введите букву1: "))
b = (input("введите букву2: "))

dicti = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10}

c = dicti.get(a) - dicti.get(b)
if c > 0:
    c = c - 1
else:
    c = abs(c + 1)
print(f"количество букв между {c}, номер первой буквы {dicti.get(a)}, номер второй {dicti.get(b)}")