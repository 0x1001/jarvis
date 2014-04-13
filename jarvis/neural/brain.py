################################################################################
################################### Class ######################################
################################################################################
class BrainException(Exception): pass

class Brain(object):
    """
        Brain class - Neural network abstraction

        Attributes:
        _net        - Neural network
        _input      - Network inputs count
        _output     - Network outputs count
        _hidden     - Network hidden nodes count
    """
    def __init__(self):
        self._net = None
        self._input = 0
        self._output = 0
        self._hidden = 0

    def configure(self,input,output):
        """
            This function configures brain

            Input:
            input       - Input size
            output      - Output size

            Returns:
            Nothing
        """
        from pybrain.tools.shortcuts import buildNetwork

        if not isinstance(input,int) or not isinstance(output,int):
            raise BrainException("Bad input. Three int expected.")

        self._input = input
        self._output = output
        self._hidden = int(round((input + output)*2/3)) + 20

        self._net = buildNetwork(self._input,self._hidden,self._output)

    def learn(self,dataset):
        """
            This function trains network

            Input:
            dataset     - Dataset to train network

            Returns:
            Nothing
        """
        from pybrain.supervised.trainers import BackpropTrainer
        from pybrain.datasets import SupervisedDataSet
        from neuraltrainer import NeuralTrainer

        if self._net == None: raise BrainException("Brain is not configured!")
        if dataset == {}: raise BrainException("Dataset for learning is empty.")

        data = SupervisedDataSet(self._input,self._output)
        for input,output in dataset.items():
            input = self._normalize(input,self._input)
            output = self._normalize(output,self._output)
            data.addSample(input,output)
            data.addSample(input,output)# For better learning 2x

        trainer = NeuralTrainer(self._net, data)
        trainer.trainUntilConvergence()

    def think(self,data):
        """
            Activates brain with data and produces response

            Input:
            data        - Input data (request)

            Returns:
            output data (answer)
        """
        if self._net == None: raise BrainException("Brain is not configured!")

        data = self._normalize(data,self._input)
        return self._denormalize(map(lambda data: int(round(data)),self._net.activate(data)))

    def _normalize(self,data,norm):
        """
            Adjust data to proper length

            Input:
            data        - List to adjust
            norm        - Norm used for adjusting

            Returns:
            adjusted data
        """
        if len(data) > norm:
            data = data[:norm]
        elif len(data) < norm:
            data += (0,)*(norm - len(data))

        return data

    def _denormalize(self,data):
        """
            Removes zeros from data

            Input:
            data        - List with int

            Returns:
            data without zeros
        """
        return [element for element in data if element != 0]