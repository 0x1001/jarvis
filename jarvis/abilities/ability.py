################################################################################
################################### Class ######################################
################################################################################
class AbilityException(Exception): pass

class Ability(object):
    """
        Ability abstract class

        Attributes:

    """
    def execute(self):
        """
            Executes ability

            Input:
            Nothing

            Returns:
            Nothing
        """
        raise AbilityException("Not implemented.")
