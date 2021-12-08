"""Python functions for JavaScript Trials 1."""


def output_all_items(items):

    for item in items:
         print(item)

def get_all_evens(nums):
    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)

    return even_nums

def get_odd_indices(items):

    result =[]
    for i, item in enumerate(items):
        if i % 2 != 0:
            result.append(item)
    return result

def print_as_numbered_list(items):

    i = 0

    for item in items:
        print(f"{i}. {item}")
        i += 1


def get_range(start, stop):

    nums = []
    num = start
    while num < stop:
        nums.append(num)
        num +=1

def censor_vowels(word):

    chars = []

    for letter in word:
        if letter in "aeiou":
            chars.append("*")
        else:
            chars.append(letter)

    return "".join(chars)


def snake_to_camel(string):

    camelCase = []
    for word in string.split("_"):
        camelCase.append(f"{word[0].upper()}{word[1:]}")
    
    return "".join(camelCase)


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
