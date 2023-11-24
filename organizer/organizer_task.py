import time

from manager.RadixFormatManager import init_format
from serialize import CSVSerializer
from util import DataFrameUtil


def init_dataframe(data_frame):
    initial_epoch = round(time.time() * 1000)
    print('[!] Iniciando proceso de formato de radicados...')

    if not DataFrameUtil.isvalid(data_frame):
        print('[!] El dataframe no es válido.')
        return

    init_format(data_frame)
    final_epoch = round(time.time() * 1000)
    print(f'[!] Se cargaron {len(data_frame)} registros desde el dataframe.')
    print(f'[!] Finalizado en: {str((final_epoch - initial_epoch) / 1000)} segundos')
    return data_frame


def init_path(input_path, output_path):
    initial_epoch = round(time.time() * 1000)
    print('[!] Iniciando proceso de formato de radicados...')
    data_frame = CSVSerializer.deserialize(input_path)
    init_format(data_frame)
    CSVSerializer.serialize(output_path, data_frame)
    final_epoch = round(time.time() * 1000)
    print(f'[!] Se cargaron {len(data_frame)} registros de: {input_path}')
    print(f'[!] Finalizado en: {str((final_epoch - initial_epoch) / 1000)} segundos')
