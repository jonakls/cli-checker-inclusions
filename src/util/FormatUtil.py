import re as regex  # Library for regular expressions
import datetime

number_pattern = r'[0-9]*'

splitters = {
    '-': '',
    '/': '',
    '.': '',
    ',': '',
    ':': '',
    ';': '',
    '|': ''
}


def clean_numbers(value):
    list_numbers = regex.findall(number_pattern, str(value))
    number_value = ''
    for number in list_numbers:
        number_value += number

    return number_value


def is_short(value):
    clean_value = clean_numbers(value)
    if len(clean_value) <= 10:
        return True
    return False


def is_long(value):
    clean_value = clean_numbers(value)
    if len(clean_value) >= 11:
        return True
    return False


def fill_process(process):
    if len(process) < 5:
        for i in range(0, 5 - len(process)):
            process = '0' + process
    return process


# TODO: Prioritize 2023-00260 with final zero
def cut_process(process):
    if len(process) > 5:
        for i in range(0, len(process) - 5):
            process = process[:-1]
    return process
