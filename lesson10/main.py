# a = 2
# b = 5


# def addition(number1, number2):
#     return number1 - number2


# # print(number1)

# c = addition(10, 15)

# print(c)


# def print_smth():
#     print("Hello world!")


# a = print_smth()


# print(a)


# my_list = [1, 2, 3]

# my_list = my_list.append(4)

# print(my_list)

# import random


# def get_random_number():
#     number = random.randint(0, 10)
#     print("asdf" + number)


# print("Hello world")


# def __get_something():
#     print("asdf")


# __get_something()


# def find_sum(num1, num2):
#     """Returns the sum of num1 and num2."""
#     return num1 + num2  # Returns the sum of the numbers


# variable = find_sum(5, 10)
# variable = find_sum(variable, 5)

# print(variable)


# def even_odd(num):

#     """
#     Returns "even" if num is even, and "odd" if num is odd.
#     Parameters:
#         num (int): Any integer    Returns:
#         type (string): "even" if num is even; "odd" if num is odd
#     """

#     if num % 2 == 0:  # Checks if num/2 has a remainder of 0
#         return "even"  # If it has a remainder of 0, return "even"
#     else:
#         return "odd"  # If it doesn't, return "odd"


# number = 10

# if even_odd(number) == "even":
#     print(f"My number: {number} is even!")
# else:
#     print(f"My number: {number} is not even")


# def check_if_exist(a=None):
#     if a:
#         return a


# a = check_if_exist("A")
# print(a)


# def find_subtraction(num1, num2=50, print_result=False):
#     """Returns the sum of num1 and num2."""
#     sum_nums = num1 - num2  # Finds the sum of num1 and num2
#     if print_result:
#         print(sum_nums)
#     return sum_nums  # Returns the sum of the numbers


# find_subtraction(5, print_result=True)


# def add_two_int_numbers(a: int, b: int) -> int:
#     return a + b


# number1 = add_two_int_numbers(1.1, "50")
# print(number1)


# type_annotation_int: int = 43
# type_annotation_float: float = 2.54
# type_annotation_string: str = "efe"
# type_annotation_bool: bool = True


# from typing import List, Tuple, Dict, Union, Optional
# import random

# Dicttype_annotation_tuple: Tuple[str] = ("1", "2", "3")

# type_annotation_list: List[str] = ["a", "b", "c"]

# type_annotation_dict: Dict[str, int] = {"a": 1, "b": 2}


# def get_random_object() -> Union[int, str, List[str]]:
#     number = random.randint(0, 3)
#     if number == 0:
#         return 0
#     elif number == 1:
#         return "str"
#     else:
#         return ["1", "2", "3"]


# def another_function(number: int) -> Optional[int]:
#     if number > 10:
#         return number
#     else:
#         return None


# number1: int = another_function(1)
# print(number1)


from typing import Tuple, Optional, Union, List


# def the_func(x: Union[int, float], y: List[str], z: Optional[float] = None) -> str:
#     return "You called the_func with " + str(x) + str(y) + str(z)


# print(the_func(2, ["1", "2"]))


type_annotation_list: List[Union[float, int]] = [1.23, 3.32, 1, 3]
