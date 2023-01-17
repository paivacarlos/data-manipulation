class Foo:
    def __init__(self):
        self.public = 'Attribute accessed'
        self._protected = 'Attribute protected'
        self.__privated = 'Attribute privated'

    def public_method(self):
        return 'method public'

    def _protected_method(self):
        return 'protected method'

    def __method_privated(self):
        return 'privated method'

f1 = Foo()
print(f1.public)
print(f1.public_method())