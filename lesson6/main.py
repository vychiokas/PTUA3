# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

# my_list = []
# if age >= 18:
#     print("You are allowed to enter")
#     my_list.append(name)
# elif age == 5:
#     print("You entered 5!")
# elif age < 5:
#     print("it is less than 5")
# else:
#     print(f"you have entered {age}")


# print(my_list)

# if len("apple") < len("apples"):
#     print("it exists !")


# a = 200
# b = 450
# print("A") if a > b else print("B")


# a = 200
# b = 200
# print("A") if a > b else print("=") if a == b else print("B")


# a = 200
# b = 600
# c = 500
# print(c > a)
# print(c > b)
# if c > a and c > b:
#     print("C is the greatest of them all!")


# a = 200
# b = 400
# c = 500
# if b > a or b > c:
#     print("B is at least greater than one of the values !")


# print(not False or False)


# x = 21

# if x > 10:
#     print("Above ten")
#     if x > 20:
#         print("and also above 20!")
#     else:
#         print("but not above 20.")

# a = 50
# b = 80

# if b > a:
#     pass

# name = "Vytautas"

# if name == "Tom":
#     print("Nice to see you Tom")
# else:
#     print("welcome, user")


# user = "Olbert"
# # privileged_users = ["Tom", "Albert", "Stephen"]
# if user.startswith("A"):
#     print(f"Welcome home {user}")
# else:
#     print("INTRUDER ALLERT. Silently calling police...")


# my_dict = {"name": "Steven", "born": "1955-02-24", "interests": "Apples"}

# if my_dict["name"] == "Stephen":
#     print("This guy does not like Windows")
# else:
#     print("No clue who this is")


# my_dict = {"name": "Bill", "born": "1955-10-28", "interests": "small software"}
# if "Bill" in my_dict.values():
#     print("This guy hates apples")
# else:
#     print("No clue who this is")


# name = ""

# if not name:
#     print("Name was not entered")

# else:
#     print("name was entered")

import random

my_list = []
if my_list:
    print("items exist in list")
else:
    print("list is empty")
