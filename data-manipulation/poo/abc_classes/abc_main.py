from abc import ABC, abstractmethod

class Log(ABC):
    @abstractmethod
    def _log(self, msg):
        ...

    def log_error(self,msg):
        return self._log(f'Error: {msg}')

    def log_success(self,msg):
        return self._log(f'Success: {msg}')

class Log_print_mixin(Log):
    def _log(self, msg):
        print(f'{msg} from {self.__class__.__name__}')

l = Log_print_mixin()
l.log_success('Hi')