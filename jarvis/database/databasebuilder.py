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
                if not line.strip() == "":
                    database.add(line.strip())

        return database

class AbilitiesDataBaseBuilder(object):
    """
        Abilities builder

        Attributes:
        _jarvis         - Jarvis reference
    """
    def __init__(self):
        self._jarvis = None

    def jarvis(self,jarvis):
        """
            Sets jarvis

            Input:
            Jarvis

            Returns:
            Nothing
        """
        self._jarvis = jarvis

    def generateDataBase(self):
        """
            Generates abilities list

            Input:
            Nothing

            Returns:
            Abilities
        """
        from jarvis import Jarvis
        from database import AbilitiesDataBase
        from abilities import a_test
        from abilities import a_time
        from abilities import a_hello
        from abilities import a_exit
        from abilities import a_mediacenter
        from abilities import a_weather

        if not isinstance(self._jarvis,Jarvis): raise DataBaseBuilderException

        abilities_list = AbilitiesDataBase()
        abilities_list.addAbility(0,a_test.Test())
        abilities_list.addAbility(1,a_time.Time())
        abilities_list.addAbility(2,a_hello.Hello())

        exit_ability = a_exit.Exit()
        exit_ability.jarvis(self._jarvis)
        abilities_list.addAbility(3,exit_ability)

        mc = a_mediacenter.MediaCenter()
        abilities_list.addAbility(4,mc.factoryBBCRadioStart())
        abilities_list.addAbility(5,mc.factoryStop())

        abilities_list.addAbility(6,a_weather.Weather())

        return abilities_list

