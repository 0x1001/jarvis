################################################################################
################################### Class ######################################
################################################################################
class JarvisException(Exception): pass

class Jarvis(object):
    """
        Main Jarivs class

        Attributes:
        _brain          - Brain object
    """
    def __init__(self):
        import brain
        self._brain = brain.Brain()
        self._word_db = None

    def respond(self,request):
        """
            This method responds to request

            Input:
            request     - Request (string)

            Returns:
            answer
        """
        from database import DataBaseException

        if self._word_db == None: raise JarvisException("Don't have dictionary.")

        try:
            request = tuple(self._word_db.multipleWordId(request.split(" ")))
        except DataBaseException as error: raise JarvisException("Don't understand: " + request)

        answer = self._brain.think(request)

        try:
            answer = " ".join(self._word_db.multipleIdWord(answer))
        except DataBaseException as error: raise JarvisException("Cannot replay to this request: " + request)

        return answer

    def dictionary(self,word_database):
        """
            This method sets words database

            Input:
            word_database       - Word database

            Returns:
            Nothing
        """
        self._word_db = word_database

    def train(self,training_database):
        """
            Trains Jarvis brain

            Input:
            Traning database

            Returns:
            Nothing
        """
        from trainer import Trainer

        if self._word_db == None: raise JarvisException("Don't have dictionary.")

        trainer = Trainer(self._word_db,training_database)
        trainer.train(self._brain)
