from numbers import helper

"""
Master of Numbers - package to convert a string representation to an integer

Queiroz, Marcos - 2023

Engine Methods
    input_number
    call_method
    convert_unique_numbers
    convert_up_to_hundred
    convert_up_to_thousand
    convert_over_thousand
"""

unique_numbers = [
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]

multiples_rounded = [
    "",
    "",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]

millions_num = {
    1: 'thousand',
    2: 'million',
    3: 'billion',
    4: 'trillion',
    5: 'quadrillion',
    6: 'quintillion',
    7: 'sextillion',
    8: 'septillion',
    9: 'octillion',
    10: 'nonillion',
    11: 'decillion',
}


class MasterOfNumbers:

    def __init__(self, value):
        self.value = value

    def input_number(self):

        return MasterOfNumbers.call_method(self)

    def call_method(self):
        """
        call methods for:

        conversion from 0 to 19
        convert from 20 to 99
        convert 100 to 999
        conversion from 1000 to 999 quintillion
        """

        if self.value <= 19:
            return MasterOfNumbers.convert_unique_numbers(self)
        elif 19 < self.value <= 99:
            return MasterOfNumbers.convert_up_to_hundred(self)
        elif 99 < self.value <= 999:
            return MasterOfNumbers.convert_up_to_thousand(self)
        else:
            return MasterOfNumbers.convert_over_thousand(self)

    def convert_unique_numbers(self):
        """
        convert inputs from 0 to 19

        """
        return unique_numbers[self.value]

    def convert_up_to_hundred(self):
        prefix = multiples_rounded[self.value // 10]
        sufix = unique_numbers[self.value % 10]
        if sufix == "":
            return f"{prefix}"
        return f"{prefix}-{sufix}"

    def convert_up_to_thousand(self):
        """
        convert inputs from 100 to 999
        """
        y = self.value
        x = 100
        millions_num = 'hundred'
        return helper.merge_values(MasterOfNumbers(y // x).input_number(),
                                   millions_num, MasterOfNumbers(y % x).input_number())

    def convert_over_thousand(self):

        """
        cover inputs from 1000 to 999_999_999_999_999_999_999_999_999_999_999
        """
        for millions_num_index, millions_num_value in millions_num.items():
            if self.value < 1000 ** (millions_num_index + 1):
                break
        x = 1000 ** millions_num_index
        y = millions_num_value
        z = self.value

        return helper.merge_values(MasterOfNumbers(z // x).input_number(),
                                   y, MasterOfNumbers(z % x).input_number())
