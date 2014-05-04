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

    def _readFileContents(self,file_path):
        """
            Reads file contents

            Input:
            file_path   - Path to file

            Returns:
            list of lines
        """
        import lowlevel

        try: return lowlevel.readFileContents(file_path)
        except lowlevel.LowLevelException as error: raise DataBaseBuilderException("Cannot open: " + file_path + " . Error: " + str(error))

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
        from record import Record

        words = set()
        for file_path in self._file_list:
            contents = self._readFileContents(file_path)
            words = words.union(WordParser(contents).wordsSet())

        word_db = WordDataBase()
        word_db.addWord(Record("")) # Index 0 is not used.
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
        from wordparser import WordParser

        database = TrainingDataBase()

        for file_path in self._file_list:
            contents = self._readFileContents(file_path)

            for line in contents.split("\n"):
                data = line.split(";")
                if len(data) == 2:
                    request = WordParser(data[0]).wordsList()
                    answer = WordParser(data[1]).wordsList()
                    database.add(request,answer)

        return database


class InnerVoiceDataBaseBuilder(DataBaseBuilder):
    """
        Internal voice data base builder

        Attributes:

    """
    def generateDataBase(self):
        from database import InnerVoiceDataBase

        database = InnerVoiceDataBase()

        for file_path in self._file_list:
            contents = self._readFileContents(file_path)
            for line in contents.split("\n"):
                database.add(line)

        return database

class AbilitiesDataBaseBuilder(object):
    """
        Abilities builder

        Attributes:

    """
    def generateDataBase(self):
        """
            Generates abilities list

            Input:
            Nothing

            Returns:
            Abilities
        """
        from database import AbilitiesDataBase
        from abilities import a_test
        from abilities import a_time
        from abilities import a_hello

        abilities_list = AbilitiesDataBase()
        abilities_list.addAbility(a_test.Test())
        abilities_list.addAbility(a_time.Time())
        abilities_list.addAbility(a_hello.Hello())

        return abilities_list

