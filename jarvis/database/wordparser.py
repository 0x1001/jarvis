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
        ABILITIE        - Abilitie regex
        WORD            - Word regex
        _text           - Text contents
        _word_re        - Regular expression for a word
        _abilitie_re    - Regular expression for a abilitie
        _combined_re    - Regular expression combined
    """
    ABILITIE = "\[[0-9]+\]"
    WORD = "[a-zA-Z]+"

    def __init__(self,text):
        import re

        self._text = text
        self._abilitie_re = re.compile(self.ABILITIE)
        self._word_re = re.compile(self.WORD)
        self._combined_re = re.compile(self.WORD + "|" + self.ABILITIE)

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
        for word in self._combined_re.findall(self._text):
            words.append(self._convert(word))

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
        for word in self._combined_re.findall(self._text):
            words.add(self._convert(word))

        return words

    def _convert(self,input_str):
        """
            Converts string to Records

            Input:
            input_str   - String input

            Returns:
            Record
        """
        from record import AbilitieRecord, WordRecord

        if self._word_re.match(input_str):
            return WordRecord(input_str)
        elif self._abilitie_re.match(input_str):
            return AbilitieRecord(input_str)
        else:
            raise WordParserException("Cannot convert string to record: " + input_str)
