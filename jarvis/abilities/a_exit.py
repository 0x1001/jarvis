from ability import Ability

class Exit(Ability):
    def __init__(self):
        self._jarvis = None

    def jarvis(self,jarvis):
        """
            Sets Jarvis

            Input:
            jarvis      - Jarvis ref

            Returns:
            Nothing
        """
        self._jarvis = jarvis

    def execute(self):
        """
            Raises SystemExit

            Input:
            Nothing

            Returns:
            List of word records
        """
        from database import WordRecord

        self._jarvis.stop()

        return [WordRecord("good"),WordRecord("bye")]