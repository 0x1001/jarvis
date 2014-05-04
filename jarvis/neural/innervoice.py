################################################################################
################################### Class ######################################
################################################################################
class InnerVoiceException(Exception): pass

class InnerVoice(object):
    """
        Jarvis internal voice

        Attributes:
        _innervoice_thread     - Internal voice thread
    """
    def __init__(self):
        import threading

        self._innervoice_thread = threading.Thread(target=self._innervoice)
        self._innervoice_thread.setDaemon(True)

        self._jarvis = None
        self._database = None

    def start(self):
        """
            Starts internal voice

            Input:
            Nothing

            Returns:
            Nothing
        """
        self._innervoice_thread.start()

    def jarvis(self,jarvis):
        """
            Sets internal voice owner

            Input:
            jarvis      - Jarvis reference

            Returns:
            Nothing
        """
        self._jarvis = jarvis

    def innerVoices(self,database):
        """
            This method sets internal voices database

            Input:
            database        - Internal voices database

            Returns:
            Nothing
        """
        self._database = database

    def _innervoice(self):
        """
            Internal voice

            Input:
            Nothing

            Returns:
            Nothing
        """
        import time
        import random
        from database import DataBaseException

        if self._jarvis == None: raise InnerVoiceException("Jarvis is not set!")
        if self._database == None: raise InnerVoiceException("Innervoice database is not set!")

        while True:
            time.sleep(random.randint(30,180))

            try: self._jarvis.respond(self._database.getRandom())
            except DataBaseException: pass

