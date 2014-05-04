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

        if self._jarvis == None: raise InnerVoiceException()

        while True:
            pass

