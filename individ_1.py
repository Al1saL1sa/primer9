def fun1(a):
    global t
    if t ==0:
        x = a / 2
    else:
        x = a
    def fun2(b):
        nonlocal x
        return b * x
    return fun2


print("Введите a: ")
a = int(input())
print("Введите b: ")
b = int(input())
print("Введите 0, если фигура треугольник, 1, если фигура прямоугольник: ")
t = int(input())
n = fun1(a)
print(n(b))