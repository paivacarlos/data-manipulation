class My_string(str):
    def upper(self):
        print('Called upper!')
        return super().upper()

_string = My_string('adolfo')
print(_string.upper())