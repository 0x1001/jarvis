################################################################################
################################### Class ######################################
################################################################################
class VoiceException(Exception): pass

class Voice(object):
    """
        This class is responsible for voice speaking

        Attributes:
        _engine         - Speak engine

    """
    def __init__(self):
        import pyttsx
        self._engine = pyttsx.init()

    def speak(self,sentence):
        """
            This function says sentence

            Input:
            sentence        - String sentence

            Returns:
            Nothing
        """
        if isinstance(sentence,list):
            sentence = " ".join(sentence)
        elif isinstance(sentence,str): pass
        else:
            raise VoiceException

        self._engine.say(sentence)
        self._engine.runAndWait()

    def _test(self):
        """
            This function tests pyttsx functionality

            Input:
            Nothing

            Returns:
            Nothing
        """
        self._engine.setProperty('volume',0.1)
        self.speak("test")
        self._engine.setProperty('volume',0.5)
        self.speak("test")
        self._engine.setProperty('volume',1)
        self.speak("test")

        self._engine.setProperty('rate',100)
        self.speak("test")
        self._engine.setProperty('rate',200)
        self.speak("test")
        self._engine.setProperty('rate',300)
        self.speak("test")

        self._engine.setProperty('rate',200)

        for idx,voice in enumerate(self._engine.getProperty("voices")):
            self._engine.setProperty('voice', voice.id)
            self.speak("voice " + str(idx + 1))
