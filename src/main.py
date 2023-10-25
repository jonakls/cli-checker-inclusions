import time

import serialize.CSVSerializer as Serializer
from manager.radix.RadixFormatManager import RadixFormatManager

input_path = 'E:\\Testing\\Litigando\\RadicadosMasivos\\VM_CIVILES_GRANDE.txt'
output_path = 'E:\\Testing\\Litigando\\RadicadosMasivos\\RADICADOS_RESUELTOS.csv'


def init():
    initial_epoch = round(time.time() * 1000)
    print('[!] Iniciando proceso de serialización...')
    data_frame = Serializer.deserialize(input_path)
    print('[!] Serialización finalizada.')

    print('[!] Iniciando proceso de formateo...')
    radix_manager = RadixFormatManager(data_frame)
    print('[!] Formateo finalizado.')
    Serializer.serialize(output_path, data_frame)

    final_epoch = round(time.time() * 1000)
    print('[!] Corrido en un tiempo de: ' + str(final_epoch - initial_epoch) + 'ms')


init()
