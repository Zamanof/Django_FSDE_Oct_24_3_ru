# Closure - замыкание

"""
def outer(...):
    state = value
    def inner():
        use state
    return inner
"""

def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

clicks = make_counter()
print(clicks())
print(clicks())
print(clicks())
print(clicks())
print(clicks())