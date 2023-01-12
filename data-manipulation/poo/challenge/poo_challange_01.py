class Model:
    def __init__(self):
        self._model = None

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

class Engine:
    def __init__(self):
        self._engine = None

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, engine):
        self._engine = engine

class Factory:
    def __init__(self):
        self._factory = None

    @property
    def factory(self):
        self._factory

    @factory.setter
    def factory(self, factory):
        self._factory = factory

class Car:
    def __init__(self):
        self.model = Model()
        self.engine = Engine()
        self.factory = Factory()

    def return_car(self):
        print(self.model, self.engine, self.factory)

focus = Car()
focus.model = 'Focus'
focus.engine = '1.6'
focus.factory = 'Ford'
focus.return_car()

uno = Car()
uno.model = 'Uno'
uno.engine = '1.0'
uno.factory = 'Fiat'
uno.return_car()