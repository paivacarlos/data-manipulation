class Pencil:
    def __init__(self, cor):
        self._cor = cor

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, valor):
        self._cor = valor

pencil_01 = Pencil('blue')
pencil_01.cor = 'pink'
print(pencil_01.cor)