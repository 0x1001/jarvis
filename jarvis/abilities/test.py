from ability import Ability

class Test(Ability):
    def execute(self):
        """
            Test ability

            Input:
            Nothing

            Returns:
            Nothing
        """
        from database import WordRecord
        return [WordRecord("test")]