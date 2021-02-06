'''Задание 1'''
text ="Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects. Python is dynamically-typed and garbage-collected."
print ("p =", text.count('p'), '\n', "o=", text.count('o'))

'''Задание 2'''
from math import sqrt, pi
print('Введите массу груза')
m=float(input())
print('Введите коэффициент жесткости пружины')
k=float(input())
def function():
    w=sqrt(k/m)
    T=2*pi*sqrt(m/k)
    print(w, '\n', T)
function()

'''Задание 3'''
x=float(input("Введите число x" '\n'))
y=float(input("Введите число y" '\n'))
def function():
    summ = x+y
    com = x*y
    if (y!=0):
        div = x/y
    else:
        print(" Ты CLOWN")
        div ="не существует" 
    sub = x-y
    power = x**y
    print (" Сумма =", summ, '\n', "Деление =", div , '\n', "Произведение =", com, '\n', "Разность =", sub , '\n', "Степень =", power, '\n')
function()
        

