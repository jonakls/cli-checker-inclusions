import model.RadixModel as RadixModel


def init():
    starter_model = RadixModel.RadixModel()

    starter_model.__add__(1, 'AAAAAAA')
    starter_model.__add__(2, 'BBBBBBB')
    starter_model.__add__(3, 'CCCCCCC')

    print(starter_model)


init()
