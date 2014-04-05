################################################################################
################################### Class ######################################
################################################################################
class WordParserException(Exception): pass

################################################################################
################################### Functions ##################################
################################################################################

class WordParser(object):
    """
        This class parses text contents

        Variables:
        _text           - Text contents
        _word_re        - Regular expression for a word
    """
    def __init__(self,text):
        import re

        self._text = text
        self._word_re = re.compile("[a-zA-Z]+|\[[0-9]+\]")

    def wordsList(self):
        """
            Exctracts words from text

            Input:
            text        - Input text string

            Returns:
            list of words
        """
        if not isinstance(self._text,str): raise WordParserException("Not a string!")

        words = list()
        for word in self._word_re.findall(self._text):
            words.append(word.lower())

        return words

    def wordsSet(self):
        """
            Exctracts words from text

            Input:
            text        - Input text string

            Returns:
            list of words
        """
        if not isinstance(self._text,str): raise WordParserException("Not a string!")

        words = set()
        for word in self._word_re.findall(self._text):
            words.add(word.lower())

        return words