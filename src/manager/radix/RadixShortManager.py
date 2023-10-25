import datetime

from util import FormatUtil


def format_c9(value):
    clean_value = FormatUtil.clean_numbers(value)

    if len(str(clean_value)) == 9:
        year = extract_year(clean_value)
        if year is None:
            return None
        process = extract_process(clean_value)
        if process is None:
            return None
        return str(year) + str(process)

    return str(clean_value)


def format_c10(value):
    clean_value = FormatUtil.clean_numbers(value)

    if len(str(clean_value)) == 9:
        year = extract_year(clean_value)
        if year is None:
            return None
        process = extract_process(clean_value)
        if process is None:
            return None
        return str(year) + '-' + str(process)

    return str(clean_value)


def extract_year(value):
    year = abs(int(value[0:4]))

    if year <= 1995 or year >= datetime.datetime.now().year:
        year = abs(int(value[5:9]))
        if year <= 1995 or year >= datetime.datetime.now().year:
            return None
    return year


def extract_process(value):
    process = value[4:]

    if len(process) > 5:
        process = abs(process)
        raw_value = str(process)

        if len(raw_value) > 5:
            raw_value = FormatUtil.cut_process(raw_value)
        process = FormatUtil.fill_process(raw_value)
    return process
