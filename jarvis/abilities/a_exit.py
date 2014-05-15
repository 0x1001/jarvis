from ability import Ability

class Exit(Ability):
    def execute(self):
        """
            Raises SystemExit

            Input:
            Nothing

            Returns:
            List of word records
        """
        import sys
        sys.exit()