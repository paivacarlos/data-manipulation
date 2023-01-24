#abstraction

from pathlib import Path
LOG_FILE = Path(__file__).parent / 'log.txt'
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
        msg_formatter = f'{msg} from {self.__class__.__name__}'
        print(f'Saving in log_file: {msg_formatter}')
        with open(LOG_FILE, 'a') as file:
            file.write(msg_formatter)
            file.write('\n')

class Log_print_mixin(Log):
    def _log(self, msg):
        print(f'{msg} from {self.__class__.__name__}')

if __name__ == '__main__':
    lp = Log_print_mixin()
    lp.log_error('Something!')
    lp.log_success('Nice!')
    lf = Log_file_mixin()
    lf.log_error('Something to file')
    lf.log_success('Great!')
