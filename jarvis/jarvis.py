################################################################################
################################### Class ######################################
################################################################################
class JarvisException(Exception): pass

class Jarvis(object):
    """
        Main Jarvis class

        Variables:
        _brain      - Neural network brain
    """

    def __init__(self):
        import brain
        self._brain = brain.Brain()

    def train(self):
        """
            This method trains brain

            Input:
            Nothing

            Returns:
            Nothing
        """
        import learningmaterial
        import speak

        dataset = {}
        for input,output in learningmaterial.dataset.items():
            dataset[tuple(speak.sentenceToNumbers(input.split(" ")))] = speak.sentenceToNumbers(tuple(output.split(" ")))

        self._brain.learn(dataset)

    def understand(self,data):
        """
            This method tries to understand data string

            Input:
            data        - sentence

            Returns:
            Response
        """
        import speak

        return speak.numbersToSentence(self._brain.think(speak.sentenceToNumbers(data.split(" "))))