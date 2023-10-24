import time

import serialize.CSVSerializer as Serializer

input_path = 'E:\\Testing\\Litigando\\RadicadosMasivos\\VM_CIVILES.txt'
output_path = 'E:\\Testing\\Litigando\\RadicadosMasivos\\VM_CIVILES_OUTPUT.txt'


def init():
    initial_epoch = round(time.time() * 1000)
    print('[!] Iniciando proceso de serialización...')
    # TODO: This process consume 10MiB of RAM
    #  review code for optimization this process
    all_radix = Serializer.deserialize(input_path)
    final_epoch = round(time.time() * 1000)
    print('[!] Procesando un total de: ' + str(len(all_radix)))
    print('[!] Corrido en un tiempo de: ' + str(final_epoch - initial_epoch) + 'ms')


init()
