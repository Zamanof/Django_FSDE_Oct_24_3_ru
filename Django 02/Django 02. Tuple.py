# tpl = (25,)
#
# print(type(tpl))

numb1, numb2 = 125, 217

# Classic algorithm swap
# print(f"numb1 = {numb1}, numb2= {numb2}")
# tmp = numb1
# numb1 = numb2
# numb2 = tmp
#
# print(f"numb1 = {numb1}, numb2= {numb2}")


# Math algorithm swap
# print(f"numb1 = {numb1}, numb2= {numb2}")
#
# numb2 = numb1 + numb2
# numb1 = numb2 - numb1
# numb2 = numb2 - numb1
#
# print(f"numb1 = {numb1}, numb2= {numb2}")

# Python style swap -  tuple
# print(f"numb1 = {numb1}, numb2= {numb2}")
#
# numb1, numb2 = numb2, numb1
#
# print(f"numb1 = {numb1}, numb2= {numb2}")

def foo():
    return 285, 45, 78

# print(type(foo()))
#
# a, _, c = foo()
# print(a, c)

# def infinitive_summ(*args):
#     summ = 0
#     for i in args:
#         summ += i
#     return summ
#
# print(infinitive_summ(1, 5, 782, 15))


def some(**kwargs):
    print(type(kwargs))


some(python=35, cpp=45)

