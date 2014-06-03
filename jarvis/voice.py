################################################################################
################################### Class ######################################
################################################################################
class VoiceException(Exception): pass

class Voice(object):
    """
        This class is responsible for voice speaking
        pyttsx is a little buggy thats why i have to init pyttsx engine each time.
        This causes memory leak on Windows :(.

        Attributes:
        _volume     - Voice volume
        _rate       - Voice rate
        _voice_lock - Voice lock to fix runtime error of pyttsx

    """
    def __init__(self):
        import threading

        try: import pyttsx
        except ImportError: raise VoiceException("You have to install: pyttsx")

        self._volume = 1.0
        self._rate = 100

        self._voice_lock = threading.RLock()

    def speak(self,sentence):
        """
            This function says sentence

            Input:
            sentence        - String sentence

            Returns:
            Nothing
        """
        import pyttsx

        with self._voice_lock:
            engine = pyttsx.init()

            if isinstance(sentence,list):
                sentence = " ".join(sentence)
            elif isinstance(sentence,str): pass
            else:
                raise VoiceException("Wrong sentence type: " + str(type(sentence)))

            engine.setProperty('volume',self._volume)
            engine.setProperty('rate',self._rate)
            engine.say(sentence)

            engine.runAndWait()
            engine.stop()

            del engine

    def volume(self,value):
        """
            Sets voice volume

            Input:
            value       - Volume value

            Returns:
            Nothing
        """
        if not isinstance(value,float): raise VoiceException("Volume value has to be float.")
        if value < 0.0 or value > 1.0: raise VoiceException("Volume value has be between 0 and 1.")

        self._volume = value

    def rate(self,value):
        """
            Sets words rate per min

            Input:
            value   - Rate value (int)

            Retruns:
            Nothing
        """
        if not isinstance(value,int): raise VoiceException("Volume value has to be int.")
        if value <= 0: raise VoiceException("Volume value has be grater than 0.")

        self._rate = value
