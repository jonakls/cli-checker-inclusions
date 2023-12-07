import numpy as np


def init_format(data_frame):
    from radix_organizer.manager import radix_short
    from radix_organizer.manager import radix_long
    from radix_organizer.util import format_util
    if data_frame is None:
        raise Exception('No se ha cargado ningún archivo o simplemente hubo un error al cargarlo.')

    data_frame['RADICADO_VIRGEN'] = np.nan
    data_frame['RADICADO_C9'] = np.nan
    data_frame['RADICADO_C10'] = np.nan

    data_frame['RADICADO_VIRGEN'].astype('object')
    data_frame['RADICADO_C9'].astype('object')
    data_frame['RADICADO_C10'].astype('object')

    if data_frame is None:
        raise Exception('No se ha cargado ningún archivo o simplemente hubo un error al cargarlo.')

    data_frame['RADICADO_VIRGEN'] = data_frame['RADICACION'].apply(lambda x: virgin_value(x))

    data_frame['RADICADO_C9'] = data_frame['RADICACION'].apply(lambda x: (
        radix_short.format_c9(virgin_value(x, False)) if format_util.is_short(virgin_value(x, False))
        else radix_long.format_c9(virgin_value(x, False))
    ))

    data_frame['RADICADO_C10'] = data_frame['RADICACION'].apply(lambda x: (
        radix_short.format_c10(virgin_value(x, False)) if format_util.is_short(virgin_value(x, False))
        else radix_long.format_c10(virgin_value(x, False))
    ))


def set_values(data_frame, index, value_c9, value_c10):
    data_frame.loc[index, 'RADICADO_C9'] = str(value_c9)
    data_frame.loc[index, 'RADICADO_C10'] = value_c10


def virgin_value(value, with_dot=True):
    from radix_organizer.util import format_util
    clean_value = format_util.clean_numbers(value)
    return str("." + clean_value if with_dot else clean_value)
