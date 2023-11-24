import pandas as pd
from radix_organizer import organizer_task

data_frame = pd.read_excel('E:\\Testing\\Litigando\\RadicadosMasivos\\RADIX_TESTING.xlsx')
print(data_frame)

result_dataframe = organizer_task.init_dataframe(data_frame)
print(result_dataframe)
