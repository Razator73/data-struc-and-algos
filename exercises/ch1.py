import random


# R-1.1
def is_multiple(n, m):
    return True if n % m == 0 else False


assert is_multiple(6, 3)
assert not is_multiple(7, 2)


# R-1.2
def is_even(k):
    k = k if k >= 0 else -k
    while k >= 0:
        if k == 0:
            return True
        k -= 2
    return False


assert is_even(8)
assert is_even(0)
assert is_even(-12)
assert not is_even(9)
assert not is_even(-13)


# R-1.3
def minmax(data):
    min_num = max_num = None
    for number in data:
        if not min_num and not max_num:
            min_num = number
            max_num = number
        min_num = number if number < min_num else min_num
        max_num = number if number > max_num else max_num
    return min_num, max_num


assert minmax([1, 3, 9, 10]) == (1, 10)
assert minmax([-5, 5, -3, 2]) == (-5, 5)


# R-1.4
def sum_squares(n):
    return sum((k * k for k in range(1, n)))


assert sum_squares(1) == 0
assert sum_squares(2) == 1
assert sum_squares(3) == 5
assert sum_squares(6) == 55


# R-1.5
# Used the methods here to do the last problem

# R-1.6 and R-1.7
def sum_odd_squares(n):
    return sum((k * k for k in range(1, n) if not k % 2 == 0))


assert sum_odd_squares(1) == 0
assert sum_odd_squares(2) == 1
assert sum_odd_squares(3) == 1
assert sum_odd_squares(6) == 35

# R-1.8
# j = n + k

# R-1.9
assert tuple(range(50, 90, 10)) == (50, 60, 70, 80)

# R-1.10
assert tuple(range(8, -10, -2)) == (8, 6, 4, 2, 0, -2, -4, -6, -8)

# R-1.11
assert [2 ** i for i in range(9)] == [1, 2, 4, 8, 16, 32, 64, 128, 256]


# R-1.12
def my_choice(data):
    return data[random.randrange(len(data))]


some_data = [1, 2, 4, 8, 16, 32, 64, 128, 256]
for i in range(100):
    assert my_choice(some_data) in some_data

# C-1.13
# use the slice construct [::-1]
assert [1, 2, 3][::-1] == [3, 2, 1]


# C-1.14
def odd_pair(data):
    for i in range(len(data)):
        for k in range(len(data)):
            if i != k and data[i] * data[k] % 2 != 0:
                return True
    return False


assert odd_pair([3, 5, 6, 8])
assert not odd_pair([3, 2, 8, 16])
assert not odd_pair([2, 22, 70])


# C-1.15
def is_distinct(data):
    return True if len(set(data)) == len(data) else False


assert is_distinct([1, 2, 3])
assert not is_distinct([1, 1, 2, 3])

# C-1.16
# This is due to the immutable nature of the list. We are changing the object in an alias that is being pointed at

# C-1.17
# No since this is not making any changes on the mutable list

# C-1.18
assert [x * (x + 1) for x in range(10)] == [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]

# C-1.19
assert [chr(i) for i in range(97, 97 + 26)] == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                                                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# C-1.20
def my_shuffle(data):
    shuffled_data = []
    while len(data) > 0:
        shuffled_data.append(data.pop(random.randint(0, len(data) - 1)))
    return shuffled_data


assert len(my_shuffle([8, 6, 3, 5, 7])) == len([8, 6, 3, 5, 7])
assert set(my_shuffle([8, 6, 3, 5, 7])) - {8, 6, 3, 5, 7} == set()


# C-1.21
def reverse_inputs():
    inputs = []
    while True:
        try:
            inputs.append(input('Insert some text (ctl-D to stop): '))
        except EOFError:
            break
    print()
    for some_input in inputs[::-1]:
        print(some_input)


reverse_inputs()


# C-1.22
def dot_prod(a, b):
    assert len(a) == len(b), 'Collections must be same length'
    return [a[i] * b[i] for i in range(len(a))]


assert dot_prod([1, 2, 3], [4, 5, 6]) == [4, 10, 18]

# C-1.23
some_data = [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]
i = 0
while i <= len(some_data):
    try:
        num = some_data[i]
    except IndexError:
        print("Don't try buffer overflow attacks in Python!")
    i += 1


def count_vowels(string):
    total = 0
    for char in 'aeiou':
        total += string.lower().count(char)
    return total


assert count_vowels('If you know the exact number of input') == 12


# C-1.25
def remove_punctuation(string):
    for char in string.lower():
        if char not in 'abcdefghijklmnopqrstuvwxyz ' :
            string = string.replace(char, '')
    return string


assert remove_punctuation("Let's try, Mike.") == 'Lets try Mike'


# C-1.26
def is_solution(a, b, c):
    return (a + b == c) or (a == b - c) or (a * b == c)


assert is_solution(1, 2, 3)
assert is_solution(3, 10, 7)
assert is_solution(4, 8, 32)
assert not is_solution(0, 1, 3)


# C-1.27
def factors(n):
    assert isinstance(n, int), 'Please pass an integer'
    k = 1
    big_factors = []
    while k * k < n:
        if n % k == 0:
            big_factors.append(n // k)
            yield k
        k += 1
    if k * k == n:
        yield k
    for factor in big_factors[::-1]:
        yield factor


assert tuple(factors(100)) == (1, 2, 4, 5, 10, 20, 25, 50, 100)
assert tuple(factors(73)) == (1, 73)
assert tuple(factors(36)) == (1, 2, 3, 4, 6, 9, 12, 18, 36)


# C-1.28
def norm(v, p=2):
    return sum(x ** p for x in v) ** (1 / p)


assert norm([3, 4]) == 5
assert norm([3, 4], 3) == (27 + 64) ** (1 / 3)


# P-1.29
