import util.FormatUtil as FormatUtil
from manager.radix.Manager import Manager


class RadixFormatManager(Manager):

    def format_short(self):
        pass

    def format_long(self):
        pass

    def format_radix(self, value):

        return FormatUtil.format_string(self, True)

    @staticmethod
    def extract(value):
        return FormatUtil.clean_numbers(value)
