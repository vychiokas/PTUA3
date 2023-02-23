# from typing import Any


# def check_arguments(
#     number1: int, number2: int, *args, default_settings: bool = True, **kwargs
# ) -> None:
#     if default_settings:
#         print(number1 + number2)
#     if args:
#         for argument in args:
#             print(argument)
#     if kwargs:
#         print(kwargs)


# a = 5
# check_arguments(101, 102, "something", "something", default_settings=False)


# def multiply(x: int, y: int) -> int:
#     return x * y


# print(multiply(2, 3))


# multiplication = lambda: "Hello world"


# print(multiplication())

# from typing import Callable


# def get_sum(number1: int, number2: int) -> int:
#     return number1 + number2


# def get_something_else() -> str:
#     return "something else"


# def get_function(number: int) -> Callable:
#     if number > 1:
#         return get_sum
#     else:
#         return get_something_else


# print(get_function(2)(1, 2))


# suma = get_sum

# print(suma(5, 5))

# from typing import Callable


# def my_func(n: int) -> Callable:
#     return lambda a, b, c: (a + b + c) * n


# my_doubler = my_func(10)
# # print(my_doubler)

# print(my_doubler(10, 5, 3))


multiplication = (lambda x, y: x * y)(2, 3)
print(multiplication)
