class RadixModel:

    def __init__(self):
        self.radix_formatted = {}

    def __add__(self, base_id, radix_value):
        self.radix_formatted[base_id] = radix_value

    def __sub__(self, base_id):
        del self.radix_formatted[base_id]

    def __clear__(self):
        self.radix_formatted.clear()

    def __empty__(self):
        return len(self.radix_formatted) == 0

    def __str__(self):
        return str(self.radix_formatted)

    def __get__(self, base_id):
        return self.radix_formatted[base_id]

    def __get_all__(self):
        return self.radix_formatted

    def __sizeof__(self):
        return len(self.radix_formatted)
