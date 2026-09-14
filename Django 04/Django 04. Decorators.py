# Decorators

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Some operations before")
        # print(args)
        # print(kwargs)
        result = original_function(*args, **kwargs)
        # print(f"result = {result}")
        print("Some operations after")
        return result
    return wrapper_function


@decorator_function
def my_function(numb1, numb2):
    return numb1 + numb2

@decorator_function
def other_function(numb1, numb2, numb3):
    return numb1 + numb2 * numb3

# print(my_function(1, 2))
# print(other_function(1, 2, 5))
# print(my_function(numb1=1, numb2=2))

# authorize example
def is_authorize(login:str, password:str)->bool:
    return login == 'admin' and password == 'admin'


def check_authorize(func):
    def wrapper(*args, **kwargs):
        if is_authorize(kwargs['login'], kwargs['password']):
            print('Authorize')
            return func(*args, **kwargs)
        else:
            raise Exception('401 Unauthorized')
    return wrapper





@check_authorize
def do_something(login:str, password:str):
    print('Do something')


# do_something(login='admin', password='admin')


def validate_int_arguments(func):
    def wrapper(*args, **kwargs):
        for arg in [*args, *kwargs.values()]:
            if not isinstance(arg, int):
                raise TypeError(f'{str(type(arg))[7:-1]} object cannot be interpreted as an integer')
            return func(*args, **kwargs)
    return wrapper


@validate_int_arguments
def summ(left:int, right:int)->int:
    return left + right

@validate_int_arguments
def my_range(start:int, end:int=None, step:int=1)->list[int]:
    lst = []
    if end is None:
        end = start
        start = 0
    if step < 0:
        tmp = start
        start = end
        end = tmp
        while start < end:
            lst.append(end)
            end += step
    else:
        while start < end:
            lst.append(start)
            start += step

    return lst


# print(summ(25, 65))
# print(summ("25", "65"))

print(my_range(-100, -10, 10))
print(list(range(-100, -10, 10)))

