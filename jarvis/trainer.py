################################################################################
################################### Class ######################################
################################################################################
class TrainerException(Exception): pass

class Trainer(object):
    """
        This class is responsible for traning brain

        Attributes:
        _word_db            - Words database
        _traning_db         - Traning database
    """

    def __init__(self,word_db,traning_db):
        from database import WordDataBase,TrainingDataBase

        if not isinstance(word_db,WordDataBase) or not isinstance(traning_db,TrainingDataBase):
            raise TrainerException("Bad input. Has to be WordDataBase and TrainingDataBase objects.")

        self._word_db = word_db
        self._traning_db = traning_db

    def train(self,brain_instance):
        """
            This function trains brain

            Input:
            brain_instance  - Brain object instance

            Returns:
            Nothing
        """
        from neural import Brain,BrainException

        if not isinstance(brain_instance,Brain):
            raise TrainerException("Bad input. Has to be Brain object.")

        brain_instance.configure(self._traning_db.maxRequestWordCount(),self._traning_db.maxAnswerWordCount())

        try: brain_instance.learn(self._prepareDataSet())
        except BrainException as error: raise TrainerException(error)

    def _prepareDataSet(self):
        """
            Prepares data set for brain

            Input:
            Nothing

            Returns:
            dataset
        """
        dataset = {}

        for request,answer in self._traning_db.getAll():
            request = [ word.strip() for word in request.split(" ") if word != ""]
            answer = [ word.strip() for word in answer.split(" ") if word != ""]
            dataset[tuple(self._word_db.multipleWordId(request))] = tuple(self._word_db.multipleWordId(answer))

        return dataset
