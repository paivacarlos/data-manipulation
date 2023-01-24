from log import Log_print_mixin, Log_file_mixin

class Electronic:
    def __init__(self, name):
        self._name = name
        self._turn_on = False

    def click_button_turn_on(self):
        if not self._turn_on:
            self._turn_on = True

    def click_button_turn_off(self):
        if self._turn_on:
            self._turn_on = False

class Smartphone(Electronic, Log_file_mixin):
    def click_button_turn_on(self):
        super().click_button_turn_on()

        if self._turn_on:
            msg = f'{self._name} is ON! :)'
            self.log_success(msg)

    def click_button_turn_off(self):
        super().click_button_turn_off()

        if not self._turn_on:
            msg = f'{self._name} is OFF!'
            self.log_error(msg)