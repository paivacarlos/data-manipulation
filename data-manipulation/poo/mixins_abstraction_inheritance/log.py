#abstraction

class Log:
    def _log(self, msg):
        raise NotImplementedError(
            'Implement the method!'
        )

    def log_error(self,msg):
        return self._log(f'Error: {msg}')

    def log_success(self,msg):
        return self._log(f'Success: {msg}')

class Log_file_mixin(Log):
    def _log(self, msg):
        print(msg)

class Log_print_mixin(Log):
    def _log(self, msg):
        print(f'{msg} from {self.__class__.__name__}')

if __name__ == '__main__':
    l = Log_print_mixin()
    l.log_error('Something!')
    l.log_success('Nice!')