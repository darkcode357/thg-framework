from THG.Model.BaseXmodeClass.OptionRequired import OptionRequired


class BaseOption:
    '''
    class attributes
        name = receives module name
        required = receives necessary values for the module to work
        description = receives module description
        value = receives value assigned for module operation
    '''
    name = None
    required = False
    description = None
    value = None

    def __init__(self, name=None, required=False, description=None, value=None):
        '''
        :param name:
        :param required:
        :param description:
        :param value:
        '''
        self.name = name
        self.required = required
        self.description = description
        self.value = value

    def validate_option(self):
        if self.required and self.value is None:
            raise OptionRequired(self)