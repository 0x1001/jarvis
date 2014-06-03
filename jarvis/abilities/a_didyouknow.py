from ability import Ability
from ability import AbilityException

class DidYouKnow(Ability):
    """
        This ability looks up some "did you know facts" and returns random result.

        Attributes:
        _regex          - Regex
        _url_source     - Url source
        _file_source    - File source mainly for testing
    """
    _regex = r'<li><span class="dyk">Did you know</span> <span class="dykText">(?P<did_you_know>[a-zA-Z0-9 ]*)</span></li>'
    _url_source = 'http://www.did-you-knows.com/?page='
    _file_source = None

    def execute(self):
        """
            Did you know ability. Says some random facts.

            Input:
            Nothing

            Returns:
            List of word records
        """
        from database import WordRecord

        try:
            did_you_know = self._get_didyouknow()
        except AbilityException as error:
            did_you_know = str(error)

        response = [WordRecord("sir"),WordRecord("did"),WordRecord("you"),WordRecord("know")] + [ WordRecord(word) for word in did_you_know.split()]

        return response

    def _get_didyouknow(self):
        """
            Gets random facts from http://www.did-you-knows.com/

            Input:
            Nothing

            Returns:
            result
        """
        import requests
        import random

        if self._file_source is None:
            url = self._url_source + str(random.randint(1,50))
            try:
                req = requests.get(url)
            except requests.ConnectionError:
                raise AbilityException("my favourite page does not work")
            text = req.text
        else:
            with open(self._file_source,'r') as fp:
                text = fp.read()

        did_you_know = self._parse(text)

        if did_you_know == []: raise AbilityException("my favourite page does not work")

        return random.choice(did_you_know)

    def _parse(self,text):
        """
            Parses text and finds did you know facts

            Input:
            text

            Returns:
            Nothing
        """
        import re

        regex_compiled = re.compile(self._regex)

        did_you_know = []
        for match in regex_compiled.finditer(text):
            did_you_know.append(str(match.group("did_you_know")))

        return did_you_know