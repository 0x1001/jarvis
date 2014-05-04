################################################################################
################################### Class ######################################
################################################################################
class JarvisException(Exception): pass

class Jarvis(object):
    """
        Main Jarivs class

        Attributes:
        _brain          - Brain object
        _body           - Body object
        _word_db        - Words database
        _traning_db     - Training database
    """
    def __init__(self):
        from neural import Brain
        from body import Body
        from voice import Voice
        from neural import InnerVoice

        self._brain = Brain()
        self._body = Body()
        self._voice = Voice()
        self._inner_voices = InnerVoice()
        self._inner_voices.jarvis(self)

        self._word_db = None
        self._traning_db = None

    def respond(self,request):
        """
            This method responds to request

            Input:
            request     - Request (string)

            Returns:
            answer
        """
        from database import DataBaseException
        from database import WordParser
        from body import BodyException

        if self._word_db == None: raise JarvisException("Don't have dictionary.")

        try:
            request_coded = tuple(self._word_db.multipleWordId(WordParser(request).wordsList()))
        except DataBaseException as error: raise JarvisException("Don't understand: " + request + " . Error: " + str(error))

        thought_coded = self._brain.think(request_coded)

        try:
            thought_tuple = self._word_db.multipleIdWord(thought_coded)
        except DataBaseException as error: raise JarvisException("Cannot replay to this request: " + request + " . Error: " + str(error))

        try:
            answer_tuple = self._body.do(thought_tuple)
        except BodyException as error: raise JarvisException("Cannot do this request: " + request + " . Error: " + str(error))

        answer = " ".join([word.getValue() for word in answer_tuple])

        self._voice.speak(answer)

        return answer

    def createWordsDataBase(self,builder):
        """
            This method sets words database

            Input:
            builder         - Word database builder

            Returns:
            Nothing
        """
        self._word_db = builder.generateDataBase()

    def createTrainingDataBase(self,builder):
        """
            This method builds traning database

            Input:
            builder         - Traning database builder

            Returns:
            Nothing
        """
        self._traning_db = builder.generateDataBase()

    def createInnerVoiceDatabase(self,builder):
        """
            This method builds internal voice database

            Input:
            builder     - Database builder

            Returns:
            Nothing
        """
        self._inner_voices.innerVoices(builder.generateDataBase())

    def createAbilitiesDataBase(self,builder):
        """
            This method builds abilities database

            Input:
            builder     - Abilities builder

            Returns:
            Nothing
        """
        self._body.abilitiesDataBase(builder.generateDataBase())

    def train(self):
        """
            Trains Jarvis brain

            Input:
            Nothing

            Returns:
            Nothing
        """
        from trainer import Trainer

        if self._word_db == None: raise JarvisException("Don't have dictionary.")
        if self._traning_db == None: raise JarvisException("Don't have traning database.")

        trainer = Trainer(self._word_db,self._traning_db)
        trainer.train(self._brain)

    def start(self):
        """
            This method starts Jarvis internals

            Input:
            Nothing

            Returns:
            Nothing
        """
        self._inner_voices.start()