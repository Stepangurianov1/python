'''https://drive.google.com/file/d/1Z7i3iPOvWuJOWS72tY8pGZuZkUkd3SUv/view?usp=sharing'''

import random 
minn = int(input("введите верхний порог: "))
maxx = int(input("введите верхний порог: "))
a = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j'}
si = {1:'+', 2:'-', 3:'"', 4:'$', 5:'/', 6:'>', 7:'^',8:'!',9:':',10:'('}

letter = a.get(random.randint(minn, maxx))
figure = random.randint(minn, maxx)
sign = si.get(random.randint(minn, maxx))

print(f'случайная буква {letter}')
print(f'случайное число {figure}')
print(f'случайный символ {sign}')

