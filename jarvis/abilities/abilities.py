################################################################################
################################### Class ######################################
################################################################################
class AbilitiesException(Exception): pass

class Abilities(list):
    """
        List of Jarivs abilities

        Attributes:

    """
    def append(self,function):
        """
            Adds new abilitie

            Input:
            function        - Function ref

            Returns:
            Nothing
        """
        if not hasattr(function, '__call__'): raise AbilitiesException("Not a function!")

        super(Abilities,self).append(function)