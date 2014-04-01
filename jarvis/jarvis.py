################################################################################
################################### Class ######################################
################################################################################
class JarvisException(Exception): pass

class Jarvis(object):
    """
        Main Jarivs class

        Attributes:
        _brain          - Brain object
        _word_db        - Words database
        _traning_db     - Training database
    """
    def __init__(self):
        import brain
        self._brain = brain.Brain()
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

        if self._word_db == None: raise JarvisException("Don't have dictionary.")

        try:
            request_tuple = tuple(self._word_db.multipleWordId(WordParser(request).wordsList()))
        except DataBaseException as error: raise JarvisException("Don't understand: " + request + " . Error: " + str(error))

        answer_tuple = self._brain.think(request_tuple)

        try:
            answer = " ".join(self._word_db.multipleIdWord(answer_tuple))
        except DataBaseException as error: raise JarvisException("Cannot replay to this request: " + request + " . Error: " + str(error))

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
