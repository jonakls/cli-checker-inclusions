import csv
import os


class CSVSerializer:

    def __init__(self, path):
        self.csv_file = None
        self.csv_writer = None
