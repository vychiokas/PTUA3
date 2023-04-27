# def say_hello() -> None:
#     print("hello")


# greet = say_hello

# greet()  # print 'hello'


# def say_hello() -> None:
#     print("hello")


# my_list = [1, say_hello, "something"]
# for item in my_list:
#     print(item)

# 1
# <function say_hello at 0x00000251F1AAF4C0>
# somethin


# from collections.abc import Callable


# def say_hello(*args: str) -> None:
#     print(f"hello {args}")


# def say_goodbye(*args: str) -> None:
#     print(f"goobye {args}")


# def another_function(f: Callable, *args) -> None:
#     f("Vardas")


# another_function(say_hello, "asdf")

# another_function(say_goodbye, "asdf")


# def outer():
#     print("I am function outer()!")

#     def inner():
#         print("I am function inner()!")

#     # Function outer() returns function inner()
#     return inner


# function = outer()
# print(function)
# # <function outer.<locals>.inner at 0x7f18bc85faf0>
# function()
# # I am function inner()!

# outer()()
# # I am function inner()!


# animals = ["ferret", "vole", "dog", "gecko"]
# print(sorted(animals, key=len))
# # ['dog', 'ferret', 'gecko', 'vole']


# def reverse(s):
#     return s[::-1]


# print(reverse("I am a string"))
# # 'gnirts a ma I'


# reverse = lambda s: s[::-1]
# print(reverse("I am a string"))
# # 'gnirts a ma I'


# print((lambda s: s[::-1])("I am a string"))
# # 'gnirts a ma I'


# print((lambda x1, x2, x3: (x1 + x2 + x3) / 3)(9, 6, 6))
# # 7.0
# print((lambda x1, x2, x3: (x1 + x2 + x3) / 3)(1.4, 1.1, 0.5))
# # 1.0


# def kazkas(x1, x2, x3):
#     return (x1 + x2 + x3) / 3


# print(kazkas(9, 6, 6))

# print(callable(7))

# animals = ["ferret", "vole", "dog", "gecko"]


# def reverse_len(string: str) -> int:
#     return -len(string)


# # print(sorted(animals, key=reverse_len))
# # # ['ferret', 'gecko', 'vole', 'dog']


# animals = ["ferret", "vole", "dog", "gecko"]
# print(sorted(animals, key=lambda s: -len(s)))
# # ['ferret', 'gecko', 'vole', 'dog']

# from typing import Tuple


# def func(x) -> Tuple[int]:
#     return x, x**2, x**3


# print(func(2))
# # (2, 4, 16)


# print((lambda x: {1: x, 2: x**2, 3: x**3})(3))

# print(f"--- {(lambda s: s[::-1])('I am a string')} ---")


# print(f"--- {(lambda s: s[::-1])('Hello')} ---")


# map(<f>, <iterable>)


def reverse(s):
    return str(s)[::-1]


# # print(reverse("I am a string"))


# animals = ["cat", "dog", "hedgehog", "gecko"]
# iterator = map(reverse, animals)


# for item in iterator:
#     print(item)
# # <map object at 0x7fd3558cbef0>


# animals = ["cat", "dog", "hedgehog", "gecko"]
# iterator = map(lambda s: s[::-1], animals)
# print(list(iterator))

# ['tac', 'god', 'gohegdeh', 'okceg']


# print(list(map(lambda s: str(s)[::-1], ["cat", "dog", 3.14159, "gecko"])))
# ['tac', 'god', 'gohegdeh', 'okceg']

# print(3.14[0])


# def f(a, b, c):
#     return a + b + c


# print(list(map(f, [1, 2, 3], [10, 20, 30], [100, 200, 300])))
# # [111, 222, 333]


# def greater_than_100(x) -> bool:
#     return x > 100


# print(list(filter(greater_than_100, [1, 111, 2, 222, 3, 333])))
# # [111, 222, 333]


# print(list(filter(lambda x: x > 100, [1, 111, 2, 222, 3, 333])))

# print(type(range(10)))

# print(list(range(10)))


# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# def is_even(x):
#     return x % 2 == 0


# print(list(filter(is_even, range(10))))
# # [0, 2, 4, 6, 8]

# print(list(filter(lambda x: x % 2 == 0, range(10))))
# # [0, 2, 4, 6, 8]


# animals = ["cat", "Cat", "CAT", "dog", "Dog", "DOG", "emu", "Emu", "EMU"]


# def all_caps(s):
#     return s.isupper()


# print(list(filter(all_caps, animals)))
# # ['CAT', 'DOG', 'EMU']

# print(list(filter(lambda s: s.isupper(), animals)))
# # ['CAT', 'DOG', 'EMU']


# numbers = [1, 2, 3, 4, 5]

# list(map(str, numbers))


# def custom_map(function, iterable):
#     from functools import reduce

#     return reduce(
#         lambda items, value: items + [function(value)],
#         iterable,
#         [],
#     )


# print(list(custom_map(str, numbers)))

# def reverse(s):
#     return s[::-1]


# animals = ["cat", "dog", "hedgehog", "gecko"]
# iterator = map(reverse(2132), animals)
# iterator
# # <map object at 0x7fd3558cbef0>

# map(<f>, <iterable>)


# (lambda <parameter_list>: <expression>)("labas")


def greater_than_100(x):
    return x > 100


print(list(map(greater_than_100, [1, 111, 2, 222, 3, 333])))
# [111, 222, 333]


# First the program should ask if table was reserved/ not (Providing your full name) . And then if not would assign you a table
# (there is a specific number single, double or family tables) . After table is assigned to you, system should show how many free tables are and how which are reserved/occupied.
# The system must be able to show name/surname of the person of the reserved table (CLI option : enter reserved table nuber ; OUTCOME: Name/Surname/Time Reserved)

# #     After assigning table, system should show different menu options for breakfast, lunch , dinner , drinks (alcohol. alcohol free), to choose from. Special menu for vegetarian and vegan must be included too in the special menu. All menu items should have weight, preparation time in minutes, calories, and price.

# #     I have to have an option to change the order before the payment section. Thus I can delete, add more, update amount of the same order.

# #     I should be able to choose whatever I want from all menus in one ordering. After I finish, I need to see what I chosen, the full payable amount and approx waiting time for the food to be served

# #     Add an option to add tips (% from the full cost) to the final bill.

# #     After the payment , system should generate the receipt (logging)


class Person:
    def __init__(self, name):
        self.name = name

person = Person(name="Vytautas")