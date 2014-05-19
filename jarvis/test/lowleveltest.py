import unittest

class LowLevelTest(unittest.TestCase):
    def setUp(self):
        self.__dummy_file = "dummy.txt"

    def test_writeFileContents_validinput(self):
        import os
        import lowlevel

        contents = "AaAaba"

        lowlevel.writeFileContents(self.__dummy_file,contents)

        self.assertTrue(os.path.exists(self.__dummy_file))

        os.unlink(self.__dummy_file)

    def test_writeFileContents_invalidinput(self):
        import lowlevel
        import sys

        contents = None
        path = self.__dummy_file
        with self.assertRaises(lowlevel.LowLevelException):
            lowlevel.writeFileContents(path,contents)

        contents = "AaAaba"
        path = None
        with self.assertRaises(lowlevel.LowLevelException):
            lowlevel.writeFileContents(path,contents)

        if sys.platform == "win32" or sys.platform == "win64":
            contents = "AaAaba"
            path = "c::\ffff:ffff"
            with self.assertRaises(lowlevel.LowLevelException):
                lowlevel.writeFileContents(path,contents)

    def test_readFileContents_filenotexists(self):
        import lowlevel

        with self.assertRaises(lowlevel.LowLevelException):
            contents = lowlevel.readFileContents(self.__dummy_file)

    def test_readFileContents_fileexists(self):
        import os
        import lowlevel

        dummy_text = "aaa"

        with open(self.__dummy_file,"w") as fp:
            fp.write(dummy_text)

        contents = lowlevel.readFileContents(self.__dummy_file)

        self.assertEqual(contents,dummy_text)

        os.unlink(self.__dummy_file)

    def test_run_cmd(self):
        import lowlevel

        self.assertIsInstance(lowlevel.run_cmd("dir"),int)

    def test_temp_path(self):
        import lowlevel
        import os

        self.assertTrue(os.path.isdir(lowlevel.temp_path()))


    def test_remove(self):
        import lowlevel
        import os

        path = "dummy.txt"

        with open(path,"w"): pass
        lowlevel.remove(path)
        self.assertTrue(not os.path.exists(path))

        os.mkdir(path)
        lowlevel.remove(path)
        self.assertTrue(not os.path.exists(path))

    def test_windows_linux(self):
        import lowlevel

        self.assertNotEqual(lowlevel.is_linux(),lowlevel.is_windows())