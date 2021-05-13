"""https://drive.google.com/file/d/1RoOk7SiEjRNIE1X1K76AMTmSuWYVd6KL/view?usp=sharing"""

a = abs(int(input("введите трехзначное число ")))
b = a // 100
c = (a - b*100) //10
d = a % 10
print (f"ответ: {b+c+d}")
