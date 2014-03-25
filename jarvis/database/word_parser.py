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
    """
    def __init__(self,text):
        self._text = text

    def wordsList(self):
        """
            Exctracts words from text

            Input:
            text        - Input text string

            Returns:
            list of words
        """
        import re

        if not isinstance(self._text,str): raise WordParserException("Not a string!")

        word_re = re.compile("[a-zA-Z]*")
        words = set()
        for word in word_re.findall(self._text):
                words.add(word.lower())

        return words
