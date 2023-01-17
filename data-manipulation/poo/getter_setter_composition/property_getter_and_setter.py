class Pencil:
    def __init__(self, color):
        self.color = color

    @property
    def get_color(self):
        return self.color

pencil_01 = Pencil('green')
print(pencil_01.get_color)