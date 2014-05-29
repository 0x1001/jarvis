################################################################################
################################### Class ######################################
################################################################################
class DataBaseException(Exception): pass

class WordDataBase(object):
    """
        This class is database interface for accessing words

        Attributes:
        _database       - List of words
    """
    def __init__(self):
        self._database = []

    def addWord(self,word):
        """
            Adds new word to database

            Input:
            word        - Word to be added to db

            Returns:
            Nothing
        """
        from record import Record
        if not isinstance(word,Record): raise DataBaseException("Bad input. Not a Record.")

        if not word in self._database:
            self._database.append(word)
        else:
            raise DataBaseException("Word: " + word.getValue() + " is already in database.")

    def wordId(self,word):
        """
            This function gets word id from database

            Input:
            word        - Word

            Returns:
            word id
        """
        from record import Record
        if not isinstance(word,Record): raise DataBaseException("Bad input. Not a string.")

        try:
            return self._database.index(word)
        except ValueError: raise DataBaseException("Word: " + word.getValue() + " is not in database!")

    def idWord(self,id):
        """
            This function returns word that coresponds to given id

            Input:
            id      - Word id

            Returns:
            word
        """
        if not isinstance(id,int) or not id >= 0: raise DataBaseException("Bad word id: " + str(id))

        try:
            return self._database[id]
        except IndexError:
            raise DataBaseException("Id: " + str(id) + " not in database.")

    def multipleWordId(self,words):
        """
            This function gets words ids from database

            Input:
            words   - list of words

            Returns:
            list of words ids
        """
        return map(self.wordId,words)

    def multipleIdWord(self,ids):
        """
            This function returns list of words that corespond to list of ids

            Input:
            ids     - List of word ids

            Returns:
            list of words
        """
        return map(self.idWord,ids)

class TrainingDataBase(object):
    """
        Database for traning materials

        Attributes:
        _database       - Dictionary of strings
    """
    def __init__(self):
        self._database = {}

    def add(self,request,answer):
        """
            Adds request and answer for that request

            Input:
            request     - Request
            answer      - Answer for request

            Returns:
            Nothing
        """
        if not isinstance(request,list) or not isinstance(answer,list): raise DataBaseException("Bad input. Not a tuple.")

        self._database[tuple(request)] = tuple(answer)

    def getAll(self):
        """
            Returns all database elements in form of two lists

            Input:
            Nothing

            Returns:
            list of request,list of answer
        """
        returns_list = []
        for key,item in self._database.items():
            returns_list.append((list(key),list(item)))

        return returns_list

    def maxRequestWordCount(self):
        """
            Counts word in requests. Returns max word count.

            Input:
            Nothing

            Returns:
            Maximal count of words in requests
        """
        try: return max(map(lambda request: len(request),self._database.keys()))
        except ValueError: return 0

    def maxAnswerWordCount(self):
        """
            Counts word in answers. Returns max word count.

            Input:
            Nothing

            Returns:
            Maximal count of words in answers
        """
        try: return max(map(lambda request: len(request),self._database.values()))
        except ValueError: return 0

class InnerVoiceDataBase(object):
    """
        Internal voice database

        Attributes:
        _database       - List of internal voices
    """
    def __init__(self):
        self._database = set()

    def add(self,voice):
        """
            Adds new element

            Input:
            voice       - database element (string)

            Returns:
            Nothing
        """
        self._database.add(voice)

    def getAll(self):
        """
            Returns list of all database elements

            Input:
            Nothing

            Returns:
            Nothing
        """
        return list(self._database)

    def getRandom(self):
        """
            Gets random element

            Input:
            Nothing

            Returns:
            element
        """
        import random
        if len(self._database) == 0: raise DataBaseException("Empty database.")
        return list(self._database)[random.randint(0,len(self._database) - 1)]

class AbilitiesDataBase(object):
    """
        List of Jarivs abilities

        Attributes:
        _database       - List of abilities
    """
    def __init__(self):
        self._database = {}

    def addAbility(self,id,ab):
        """
            Adds new ability

            Input:
            id          - Ability ID
            ab          - Ability object

            Returns:
            Nothing
        """
        from abilities import Ability

        if not isinstance(ab,Ability): raise DataBaseException("Not an Ability!")
        if self._database.has_key(id): raise DataBaseException("Ability already exists!")

        self._database[id] = ab

    def getAbility(self,id):
        """
            Returns ability that matches id

            Input:
            id      - Ability id

            Returns:
            Ability
        """
        try: return self._database[id]
        except KeyError: raise DataBaseException("Ability not found. Index: " + str(id))

