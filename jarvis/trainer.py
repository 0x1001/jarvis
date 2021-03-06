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

        brain_instance.configure(input=self._traning_db.maxRequestWordCount(),output=self._traning_db.maxAnswerWordCount())

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
            dataset[tuple(self._word_db.multipleWordId(request))] = tuple(self._word_db.multipleWordId(answer))

        return dataset
