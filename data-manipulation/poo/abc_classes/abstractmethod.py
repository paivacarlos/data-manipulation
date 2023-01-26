from abc import ABC, abstractmethod

class AbstractionFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    @abstractmethod
    def name(self):
        ...

    @name.setter
    def name(self, name):
        ...

class Foo(AbstractionFoo):
    def __init(self, name):
        super().__init__(name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

foo = Foo('Bar')
print(foo.name)