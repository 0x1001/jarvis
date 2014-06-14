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
        ALLOW_TIME              - Tuple with allow time to speak
    """
    def __init__(self):
        import threading
        import datetime

        self._innervoice_thread = threading.Thread(target=self._innervoice,name=self._innervoice.func_name)
        self._stop_event = threading.Event()

        self.ALLOW_TIME = (datetime.time(8,30),datetime.time(23,00))

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
        from jarvis import JarvisException

        self._jarvis.respond("hello")

        while True:
            if self._stop_event.wait(random.randint(300,600)): break

            if self._isAllowedToSpeak():
                try: self._jarvis.respond(self._database.getRandom())
                except DataBaseException: pass
                except JarvisException: pass

    def _isAllowedToSpeak(self):
        """
            Checks if it is allowed to speak

            Input:
            Nothing

            Returns:
            True/False
        """
        import datetime

        current_time = datetime.datetime.now()
        beginning = datetime.datetime.combine(current_time.date(),self.ALLOW_TIME[0])
        end = datetime.datetime.combine(current_time.date(),self.ALLOW_TIME[1])

        if current_time < beginning or current_time > end:
            return False
        else:
            return True