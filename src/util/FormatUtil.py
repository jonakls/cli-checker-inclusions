import re as regex  # Library for regular expressions

number_pattern = r'[0-9-]*'

splitters = {
    '-': '',
    '/': '',
    '.': '',
    ',': '',
    ':': '',
    ';': '',
    '|': ''
}

available_years = [
    "1985",
    "1986",
    "1987",
    "1988",
    "1989",
    "1990",
    "1991",
    "1992",
    "1993",
    "1994",
    "1995",
    "1996",
    "1997",
    "1998",
    "1999",
    "2000",
    "2001",
    "2002",
    "2003",
    "2004",
    "2005",
    "2006",
    "2007",
    "2008",
    "2009",
    "2010",
    "2011",
    "2012",
    "2013",
    "2014",
    "2015",
    "2016",
    "2018",
    "2019",
    "2020",
    "2021",
    "2022",
    "2023"
]


def format_string(text, with_splitter):
    if with_splitter:
        for splitter in splitters:
            value = value.replace(splitter, ' ')

    clean_text = regex.sub(number_pattern, ' ', text).lower()
    return clean_text


def clean_numbers(value):
    list_numbers = regex.findall(number_pattern, str(value))
    number_value = ''
    for number in list_numbers:
        number_value += number

    return number_value
