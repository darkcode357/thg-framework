from lib.thg.core.BaseXmodeClass.OptionRequired import OptionRequired


class BaseOptions:
    """
    class base para opções de metodos
    """

    options = None

    def __init__(self):
        """
        cria um lista de options
        """
        self.options = []

    def add_option(self, option):
        """
        :param option: adiciona option
        :return:
        """
        self.options.append(option)

    def get_options(self):
        """

        :return:
        """
        return self.options

    def get_option(self, name):
        """

        :param name: reccebe o valor da option
        :return:
        """
        for option in self.options:
            if option.name == name:
                return option.value
        return None

    def set_option(self, name, value):
        """

        :param name: nome da option
        :param value: valor da option
        :return:
        """
        for idx, option in enumerate(self.options):
            if option.name == name:
                option.value = value
                self.options[idx] = option

    def validate(self):
        """
        :return: verifica se a oção e valida ou não
        """
        error = []
        for option in self.get_options():
            try:
                option.validate_option()
            except OptionRequired as e:
                error.append(e)
        if error:
            return [False, error]
        else:
            return [True, None]
