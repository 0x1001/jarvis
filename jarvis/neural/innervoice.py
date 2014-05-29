################################################################################
################################### Class ######################################
################################################################################
class InnerVoiceException(Exception): pass

class InnerVoice(object):
    """
        Jarvis internal voice

        Attributes:
        _innervoice_thread      - Internal voice thread
        _stop_event             - Stop event
    """
    def __init__(self):
        import threading

        self._innervoice_thread = threading.Thread(target=self._innervoice)
        self._stop_event = threading.Event()

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
        from database import DataBaseException

        if self._jarvis == None: raise InnerVoiceException("Jarvis is not set!")
        if self._database == None: raise InnerVoiceException("Innervoice database is not set!")

        self._innervoice_thread.start()

    def stop(self):
        """
            Stops internal voice

            Input:
            Nothing

            Returns:
            Nothing
        """
        self._stop_event.set()
        if self._innervoice_thread.isAlive(): self._innervoice_thread.join()

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
        import random
        from database import DataBaseException

        self._jarvis.respond("hello")

        while True:
            if self._stop_event.wait(random.randint(180,600)): break

            try: self._jarvis.respond(self._database.getRandom())
            except DataBaseException: pass

