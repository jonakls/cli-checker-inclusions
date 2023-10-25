from manager.radix import RadixShortManager


def format_c9(value):
    if len(str(value)) == 23:
        short_value = value[12:21]
        return RadixShortManager.format_c9(short_value)

    return value


def format_c10(value):
    if len(str(value)) == 23:
        short_value = value[12:21]
        return RadixShortManager.format_c10(short_value)

    return value
