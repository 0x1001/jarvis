################################################################################
################################### Class ######################################
################################################################################
class BrainException(Exception): pass

class Brain(object):
    """
        Brain abstract class

        Attributes:

    """
    def configure(self,**kargs):
        """
            This function configures brain

            Input:
            kargs

            Returns:
            Nothing
        """
        raise BrainException("Not implemented!")

    def learn(self,dataset):
        """
            This function trains brain

            Input:
            dataset     - Dataset to train brain

            Returns:
            Nothing
        """
        raise BrainException("Not implemented!")

    def think(self,data):
        """
            Activates brain with data and produces response

            Input:
            data        - Input data (request)

            Returns:
            output data (answer)
        """
        raise BrainException("Not implemented!")
