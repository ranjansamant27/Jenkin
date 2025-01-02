# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

"""def lol(a,b):
    c=a+b
    d=a-b
    return c,d

hey,hi= lol(1,2)
print(f"{hey} \n{hi}") """
#new
'''def upd(x):
    x=10
    return x

a=upd(9)
print(a)'''


"""def me(name,age=0 ):
    print(name)
    print(age)


me("Ranjan",21)"""


"""def add(a,**b):
    print(a)
    print(b)

print(add(23,prince =31,age = 32,mom = 23))
"""

"""
a=25

def some():



    print(f"{globals()['a']}")
    a=15

    print("in function, a is",a)


some()

print("outside, a is",a)
print(id(a)) """


"""def fact(input):

    if input == 0 :
        return 1
    else:
        return input*fact(input-1)

a = int(input("number : "))
print(fact(a)) """

a= 15

def show():

    globals()["a"]
    a=18
    return("In function, value of a is",a)


print(show())
print("outside function, a's value is",a)



