"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant.
EXPECTED_BAKE_TIME = 40

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(x):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - x


#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
PREPARATION_TIME = 2

def preparation_time_in_minutes(x):
    """Calculate the preparation time.

    :param number_of_layers: int - number of layers in the lasagna.
    :return: int - total preparation time (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the number of layers in the lasagna as an argument and
    returns how many minutes it would take to prepare the lasagna based on the
    `PREPARATION_TIME`.
    """

    return PREPARATION_TIME * x



#TODO: define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)

def elapsed_time_in_minutes(x, y):
    """Calculate the elapsed time.

    :param number_of_layers: int - number of layers in the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total elapsed time (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the number of layers in the lasagna and the actual minutes
    the lasagna has been in the oven as arguments and returns how many minutes
    have elapsed based on the `PREPARATION_TIME`.
    """

    return preparation_time_in_minutes(x) + y
