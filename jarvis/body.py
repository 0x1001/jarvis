################################################################################
################################### Class ######################################
################################################################################
class BodyException(Exception): pass

class Body(object):
    """
        This class can invoke Jarvis abilites

        Attributes:
        _abilities_db       - Abilities database
    """
    def __init__(self):
        self._abilities_db = None

    def abilitiesDataBase(self,abilities_db):
        """
            Sets abilities database

            Input:
            abilities_db        - Abilities database

            Returns:
            Nothing
        """
        self._abilities_db = abilities_db

    def do(self,request):
        """
            This function performes action

            Input:
            request     - List of requests

            Returns:
            answer
        """
        from database import WordRecord,AbilityRecord
        from abilities import AbilityException
        from database import DataBaseException

        if self._abilities_db == None: raise BodyException("Abilities database not given!")

        answer = []
        for record in request:
            if isinstance(record,AbilityRecord):
                try: ability = self._abilities_db.getAbility(record.getValue())
                except DataBaseException as error: raise BodyException(error)

                try: abilitie_answer = ability.execute()
                except AbilityException as error: raise BodyException(error)

                answer += abilitie_answer
            elif isinstance(record,WordRecord):
                answer.append(record)
            else:
                print type(record)
                raise BodyException("Unknown record!")

        return answer

