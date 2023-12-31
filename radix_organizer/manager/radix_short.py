def format_c9(value):
    generic_value = generic_format(value)
    if generic_value is None:
        return ''
    if len(generic_value) == 1:
        return f'{generic_value[0]}'
    elif len(generic_value) == 2:
        return f'{generic_value[0]}{generic_value[1]}'
    return ''


def format_c10(value):
    generic_value = generic_format(value)
    if generic_value is None:
        return ''
    if len(generic_value) == 1:
        return f'{generic_value[0]}'
    if len(generic_value) == 2:
        return f'{generic_value[0]}-{generic_value[1]}'
    return ''


def generic_format(value):
    from radix_organizer.util import format_util
    clean_value = format_util.clean_numbers(value)

    if len(str(clean_value)) <= 10:
        year = format_util.extract_year(value)
        if year is None:
            return None

        if not isinstance(year, list):
            clean_value = clean_value.replace(year, "")
            process = format_util.extract_process(clean_value)
        else:
            clean_value = clean_value.replace(year[1], "")
            year = year[0]
            process = format_util.extract_process(clean_value)

        if process is None:
            return None
        return [year, process]

    year = format_util.extract_year(clean_value)
    if year is None:
        return None
    clean_value = clean_value.replace(year, "")

    return [str(clean_value)]
