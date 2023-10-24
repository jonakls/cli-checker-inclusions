import pandas as pd


def process_csv(input_path):
    return pd.read_csv(input_path, delimiter='\t', encoding='latin1')


def deserialize(input_path):
    data_frame = process_csv(input_path)
    data_frame.head()
    radix_list = data_frame[["PROCESO_ID", "RADICACION"]]
    print(radix_list)
    return radix_list


def serialize():
    pass
