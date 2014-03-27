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
        if not isinstance(word,str): raise DataBaseException("Bad input. Not a string.")

        if not word in self._database:
            self._database.append(word)
        else:
            raise DataBaseException("Word: " + word + " is already in database.")

    def wordId(self,word):
        """
            This function gets word id from database

            Input:
            word        - Word

            Returns:
            word id
        """
        if not isinstance(word,str): raise DataBaseException("Bad input. Not a string.")

        try:
            return self._database.index(word)
        except ValueError: raise DataBaseException("Word: " + word + " is not in database!")

    def idWord(self,id):
        """
            This function returns word that coresponds to given id

            Input:
            id      - Word id

            Returns:
            word
        """
        if not isinstance(id,int) or not id >= 0: raise DataBaseException("Bad word id.")

        try:
            return self._database[id]
        except IndexError:
            raise DataBaseException("Id not in database.")
