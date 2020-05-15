from THG.Model.BaseXmodeClass.OptionRequired import OptionRequired


class BaseOption:
    name = None
    required = False
    description = None
    value = None

    def __init__(self, name=None, required=False, description=None, value=None):
        self.name = name
        self.required = required
        self.description = description
        self.value = value

    def validate_option(self):
        if self.required and self.value is None:
            raise OptionRequired(self)

