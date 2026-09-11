from random import randint
# Lambda expressions

# pure functions

def add(a:int, b:int)->int:
    return a + b


# print(add(1, 2))
# print(type(add))
# func = add
#
# print(func(3,4))


def filter_negative(lst:list)->list:
    negatives = []
    for i in lst:
        if i < 0:
            negatives.append(i)
    return negatives

def filter_positive(lst:list)->list:
    positive = []
    for i in lst:
        if i > 0:
            positive.append(i)
    return positive


def my_filter(lst:list, predicate)->list:
    result = []
    for i in lst:
        if predicate(i):
            result.append(i)
    return result


def is_negative(value:int)->bool:
    return value < 0

def is_positive(value:int)->bool:
    return value > 0

def is_even(value:int)->bool:
    return value % 2 == 0

lst = [randint(-100, 100) for i in range(20)]

# print(filter_negative(lst))
# print(filter_positive(lst))

# print(my_filter(lst, is_negative))
# print(my_filter(lst, is_even))
# print(my_filter(lst, lambda x: x < 0))
# print(my_filter(lst, lambda x: x % 3 == 0))

# lambda params_list: expression

fn = lambda x: x < 0

print(type(fn))
print(type(lambda x: x < 0))

"""
C++         [](int x){ return x < 0; }

C#          (int x) => x < 0;

Python:     lambda x: x < 0
"""
