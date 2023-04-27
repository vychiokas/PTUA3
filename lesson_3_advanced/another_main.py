number = input("Please enter number:")


def get_magic_number(number):
    number_quant = len(number)
    list_of_digits = [int(i) for i in str(number)]
    list_of_digits_max = []
    for _ in range(number_quant):
        list_of_digits_max.append(str(max(list_of_digits)))
        list_of_digits.remove(max(list_of_digits))
    list_of_digits = [int(i) for i in str(number)]
    list_of_digits_min = []
    for _ in range(number_quant):
        list_of_digits_min.append(str(min(list_of_digits)))
        list_of_digits.remove(min(list_of_digits))
    number_max = "".join(list_of_digits_max)
    number_min = "".join(list_of_digits_min)
    print(int(number_max) - int(number_min))


get_magic_number(number)
