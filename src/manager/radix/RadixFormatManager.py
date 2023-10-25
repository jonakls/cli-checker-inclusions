import numpy as np

from manager.radix import RadixShortManager, RadixLongManager
from src.util import FormatUtil


class RadixFormatManager:

    def __init__(self, data_frame):
        self.data_frame = data_frame
        self.data_frame['RADICADO_C9'] = np.nan
        self.data_frame['RADICADO_C10'] = np.nan
        self.format()

    def format(self):
        if self.data_frame is None:
            raise Exception('No se ha cargado ningún archivo o simplemente hubo un error al cargarlo.')

        for index, row in self.data_frame.iterrows():
            value = row['RADICACION']
            if FormatUtil.is_short(value):
                self.data_frame.at[index, 'RADICADO_C9'] = RadixShortManager.format_c9(value)
                self.data_frame.at[index, 'RADICADO_C10'] = RadixShortManager.format_c10(value)
            elif FormatUtil.is_long(value):
                self.data_frame.at[index, 'RADICADO_C10'] = RadixLongManager.format_c10(value)
                self.data_frame.at[index, 'RADICADO_C9'] = RadixLongManager.format_c9(value)
            else:
                self.data_frame.at[index, 'RADICADO_C9'] = '0'
                self.data_frame.at[index, 'RADICADO_C10'] = '0'
