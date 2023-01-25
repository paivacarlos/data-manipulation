from .second_level_paste import second_level_file as file_02

class class_first_level_main:
    def __init__(self):
        self.msg = None

    def print_first_level_msg(self, msg):
        return print(f'msg from first level: {msg}')

    def from_first_level_file_msg_from_second_file(self, msg):
        obj = file_02.class_second_level()
        msg_02 = obj.print_sencod_level_msg(msg)
        return msg_02