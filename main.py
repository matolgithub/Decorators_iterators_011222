def decorator(function):
    def wrapper():
        full_list = function()
        print("----------------")
        new_list = [item for item in full_list if int(item) % 2 != 0]
        print(f"It is string from decorator! And new list is:\n{new_list}")
        return new_list

    return wrapper


@decorator
def example_function(x=10):
    print("It is example function")
    list_compr = [item for item in range(x)]
    print(list_compr)

    return list_compr


# example_function()


# def counter(func):
#     def wrap(*args, **kwargs):
#         wrap.count += 1
#         return func(*args, **kwargs)
#
#     wrap.count = 0
#     return wrap
#
#
# @counter
# def f():
#     return 42
#
#
# print(f())
# print(f())
# print('Число вызовов функции:', f.count)


# Iterator
def iter_func(iterable=[1, 2, 3, 4, 5, 6, 7, 8]):
    iterator = iter(iterable)
    next_element_exist = True
    while next_element_exist:
        try:
            element_from_iterator = next(iterator)
            print(f"Element number {iterable.index(element_from_iterator) + 1} - {element_from_iterator}.")
        except StopIteration:
            next_element_exist = False


iter_func()
