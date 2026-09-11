# LEGB
# L - Local
# E - Enclosing
# G - Global
# B - Built-in

from math import pi as PI

print(f'Built-in Pi = {PI}')

def foo():
    # global PI
    PI = "Salam"
    def bar():
        # nonlocal PI
        PI = True
        print(f'Local Pi = {PI}')
    bar()
    print(f'Enclosing Pi = {PI}')



PI = 25
print(f'Global Pi = {PI}')

foo()

