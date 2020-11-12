from unittest import TestCase
from lib.thg.core.Interpreter import ThgInterpreter
class thg_encodeTestCase(TestCase):
    def test_thg_encode(self):

        self.assertEqual("64",ThgInterpreter.thg_encode())
    pass