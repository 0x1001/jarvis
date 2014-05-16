################################################################################
################################### Class ######################################
################################################################################
from brain import BrainException,Brain

class LookUpTableBrainException(BrainException): pass

class LookUpTableBrain(Brain):
    """
        Brain class based on Lookup table

        Attributes:
        _table      - Look up table
    """
    def __init__(self):
        self._table = {}

    def configure(self,**kargs):
        """
            This method is not used

            Input:
            Nothing

            Returns:
            Nothing
        """
        pass

    def learn(self,dataset):
        """
            This method trains network

            Input:
            dataset     - Dataset to train

            Returns:
            Nothing
        """
        if dataset == {}: raise LookUpTableBrainException("Dataset for learning is empty.")

        self._table = dataset

    def think(self,data):
        """
            Activates brain with data and produces response

            Input:
            data        - Input data (request)

            Returns:
            output data (answer)
        """
        try: return self._table[data]
        except KeyError: raise LookUpTableBrainException("Don't know.")