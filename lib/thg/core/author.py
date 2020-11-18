###
#
# An author of a piece of code in either the framework, a module, a script,
# or something entirely unrelated.
#
###
Kn = {"darkcode0x00": ["Luiz Corrêa", "darkcode0x00@darkcode0x00.com.br"]}


class Author:
    #
    # Constants
    #
    # A hash that maps known author names to email addresses
    def __init__(self, name):
        self.name = name

    #
    # Class Methods
    #
    def author_to_mail(self):
        """

        :return: str: mail
        """
        for nome, real_name_mail in Kn.items():
            if self.name == nome:
                return real_name_mail[1]
