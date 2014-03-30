################################################################################
################################### Class ######################################
################################################################################
class DataBaseBuilderException(Exception): pass

class DataBaseBuilder(object):
    """
        Abstract database builder class

        Attributes:
        _file_list      - List of text files
    """
    def __init__(self):
        self._file_list = []

    def addTxtFile(self,path):
        """
            This function adds file to list that is used to generate word database

            Input
            path    - File path

            Returns:
            Nothing
        """
        self._file_list.append(path)

    def generateDataBase(self):
        """
            This method has to be implemented in child class.

            Input:
            Nothing

            Returns:
            database
        """
        raise DataBaseBuilderException("Not implemented!")

class WordDataBaseBuilder(DataBaseBuilder):
    """
        This class is responsible for building words database

        Attributes:

    """
    def generateDataBase(self):
        """
            This function generates word database base on list of text files

            Input:
            Nothing

            Returns:
            Word database
        """
        from database import WordDataBase
        from wordparser import WordParser
        import lowlevel

        words = set()
        for file_path in self._file_list:
            try: contents = lowlevel.readFileContents(file_path)
            except lowlevel.LowLevelException as error: raise DataBaseBuilderException("Cannot open: " + file_path + " . Error: " + str(error))

            words = words.union(WordParser(contents).wordsList())

        word_db = WordDataBase()
        for word in words: word_db.addWord(word)

        return word_db

class TrainingDataBaseBuilder(DataBaseBuilder):
    """
        This class is responsible for building traning database

        Attributes:

    """
    def generateDataBase(self):
        """
            This function generates traning database base on list of text files

            Input:
            Nothing

            Returns:
            Training database
        """
        from database import TrainingDataBase
        import lowlevel

        database = TrainingDataBase()

        for file_path in self._file_list:
            try: contents = lowlevel.readFileContents(file_path)
            except lowlevel.LowLevelException as error: raise DataBaseBuilderException("Cannot open: " + file_path + " . Error: " + str(error))

            for line in contents.split("\n"):
                data = line.split(";")
                request = data[0]
                answer = data[1]
                database.add(request,answer)

        return database