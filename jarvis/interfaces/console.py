################################################################################
################################### Class ######################################
################################################################################
class ConsoleException(Exception): pass

class Console(object):
    """
        Console interface

        Attributes:
        _console_thread     - Console thread
        _jarvis             - Jarvis reference
    """
    def __init__(self):
        import threading

        self._jarvis = None

        self._console_thread = threading.Thread(target=self._console)
        self._console_thread.setDaemon(True)

    def start(self):
        """
            Starts console thread

            Input:
            Nothing

            Returns:
            Nothing
        """
        self._console_thread.start()

    def jarvis(self,jarvis):
        """
            Sets jarvis reference

            Input:
            jarvis      - Jarvis reference

            Returns:
            Nothing
        """
        self._jarvis = jarvis

    def _console(self):
        """
            Console input handler. Blocking function.

            Input:
            Nothing

            Returns:
            Nothing
        """
        from jarvis import JarvisException

        if self._jarvis == None: raise ConsoleException()

        while True:
            request = raw_input("Ask>> ")

            try: print self._jarvis.respond(request)
            except JarvisException as error: print str(error)

