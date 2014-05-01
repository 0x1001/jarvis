import unittest

class ConsoleTest(unittest.TestCase):
    def setUp(self):
        from interfaces import Console

        self.console = Console()

    def test_start(self):
        from jarvis import Jarvis

        self.console.jarvis(Jarvis())
        self.console.start()

    def test_console(self):
        self.assertTrue(hasattr(self.console,"_console"))

    def test_console_exception(self):
        from interfaces import ConsoleException
        with self.assertRaises(ConsoleException):
            self.console._console()

