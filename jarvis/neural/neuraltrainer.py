################################################################################
################################### Class ######################################
################################################################################
from pybrain.supervised.trainers import BackpropTrainer

class NeuralTrainerException(Exception): pass
class NeuralTrainer(BackpropTrainer):
    def simpleTrain(self):
        """
            Simple neural network trainer
            This trainer overfits neural network

            Input:
            Nothing

            Returns:
            Nothing
        """
        while True:
            error = self.train()
            if error < 0.001: break

        return error,self.testOnData()