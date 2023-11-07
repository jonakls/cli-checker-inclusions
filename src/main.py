import time

import serialize.CSVSerializer as Serializer
from manager.radix import RadixFormatManager

input_path = 'E:\\Testing\\Litigando\\INGE\\ARREGLAR_RADICADOS_JONATHAN.xlsx'
output_path = 'E:\\Testing\\Litigando\\INGE\\RADICADOS_RESUELTOS.csv'


def init():
    initial_epoch = round(time.time() * 1000)
    print('[!] Iniciando proceso de formato de radicados...')
    data_frame = Serializer.deserialize(input_path)
    RadixFormatManager.init_format(data_frame)
    Serializer.serialize(output_path, data_frame)
    final_epoch = round(time.time() * 1000)
    print(f'[!] Se cargaron {len(data_frame)} registros de: {input_path}')
    print(f'[!] Finalizado en: {str((final_epoch - initial_epoch) / 1000)} segundos')


init()
