import pandas as pd


def process_csv(input_path):
    return pd.read_csv(input_path, delimiter='\t', encoding='latin1')


def deserialize(input_path):
    data_frame = process_csv(input_path)
    data_frame.head()
    radix_list = data_frame[["PROCESO_ID", "RADICACION"]]
    return radix_list


def serialize(output_path, data_frame):
    data_frame.to_csv(output_path, sep=';', index=False)
