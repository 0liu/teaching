"""
I. Given a list A, define a function to accumulate the elements of A and save
the results at each index to a new list B. B is called the cumulative sum of A.

Example:
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
"""


def calc_cum_sum(A):
    """
    Calculate the cum sum of A.
    """
    B = []
    cumsum = 0

    for x in A:
        cumsum += x
        B.append(cumsum)

    return B


"""
II. Write two functions my_int() and my_bin() to convert a binary integer string
to the decimal number, and vice versa, to convert a decimal number to a binary
integer string. You cannot use the built-in functions int() and bin() in your
code, but you can verify your code with them.

Example:
my_int(’0b10101’)  # return 21
my_bin(21)         # return ’0b10101’
"""


def my_int(s):
    """
    Convert binary integer string s to the decimal integer.
    Assume s always starts with ’0b’.

    Example: s = '0b1010'
    """
    # Your code here…
    s = s[2:]  # remove '0b' at the beginning. '0b11010' -> '11010'

    n = len(s)  # n = 5 if s = '11010'
    x = 0
    for i in range(n):
        # i:   0, 1, 2, 3, 4
        # n-i:  5, 4, 3, 2, 1
        # n-i-1: 4, 3, 2, 1, 0
        # s[i]: 1, 1, 0, 1, 0
        # a:   16, 8, 4, 2, 1
        #
        # 4: 2 * 2 * 2 * 2 = 16
        # 3: 2 * 2 * 2 = 8
        # 2: 2 * 2 = 4
        # 1: 2 = 2
        # 0: 2^0 = 1

        a = 2 ** (n - i - 1)

        # '1' -> 1
        # '0' -> 0
        if s[i] == "1":
            s_i = 1
        else:
            s_i = 0

        x = x + s_i * a

    return x


def my_bin(x):
    """
    Convert a decimal integer x to binary integer string.
    Assume prefix your returned string with ’0b’.
    """
    # Your code here…
    remainders = []
    while x != 0:
        rem = x % 2
        x = x // 2
        remainders.append(rem)

    # x: 10
    # remainders: [0, 1, 0, 1]
    remainders.reverse()  # [1, 0 , 1, 0]

    # build s from remainders
    s = "0b"
    for digit in remainders:
        s += str(digit)  # "1" + "0" + "1" + "0" = "1010"

    return s  # '0b1010'


"""
III. Write a function to convert a Roman numeral string to the decimal number.

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together.
12 is written as XII, which is simply X + II. The number 27 is written as XXVII,
which is XX + V + II. Roman numerals are usually written largest to smallest
from left to right. However, the numeral for four is not IIII. Instead, the
number four is written as IV. Because the one is before the five we subtract it
making four. The same principle applies to the number nine, which is written as
IX. There are six instances where subtraction is used:

- I can be placed before V (5) and X (10) to make 4 and 9.
- X can be placed before L (50) and C (100) to make 40 and 90.
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

"""


"""
Hint:

Replace ... with your code in the hint. Do not copy & paste.

1. Use a dictionary as a look-up table to convert Roman symbols to its values.

roman = {'M': 1000, 'D': 500, ...}

2. Use a loop to iterate over the length of roman numeral string s.

n = len(s)
for i in range(...):

3. In the loop, for each character in roman numeral string s, convert character to its value using the dictionary you built:

value = roman[...]

4. For each character value, check if:
    (1) The current character is the last element in s: i == len(s) - 1
    (2) If the value is greater than the next value: val >= roman[s[i+1]]

    If either of this two conditions is True, should you add the value to
    your result (the decimal number to be returned) or subtract it from the
    number? Use a "if...else..." structure to update your result.
"""
