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
        from brain import Brain

        if not isinstance(brain_instance,Brain):
            raise TrainerException("Bad input. Has to be Brain object.")

        #brain_instance.configure()
        brain_instance.learn(self._prepareDataSet())

    def _prepareDataSet(self):
        """
            Prepares data set for brain

            Input:
            Nothing

            Returns:
            dataset
        """
        return []