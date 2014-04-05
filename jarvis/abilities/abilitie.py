################################################################################
################################### Class ######################################
################################################################################
class AbilitieException(Exception): pass

class Abilitie(object):
    """
        Abilitie abstract class

        Attributes:

    """
    def execute(self):
        """
            Executes abilite

            Input:
            Nothing

            Returns:
            Nothing
        """
        raise AbilitieException("Not implemented.")
