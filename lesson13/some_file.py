from typing import List, Optional, Union


import random


def print_random_number(
    start_number: int, end_number: int
) -> Optional[Union[int, float]]:
    try:
        return random.randint(start_number, end_number)
    except ValueError as e:
        print(f"Error: print_random_number() {e}")


print(print_random_number(start_number=1, end_number=10.5))
