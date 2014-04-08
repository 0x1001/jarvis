################################################################################
################################### Class ######################################
################################################################################
class Record(object):
    """
        Record parent class

        Attributes:
        _value       - Record value
    """
    def __init__(self,value):
        self._value = value

    def getValue(self):
        """
            Returns record value

            Input:
            Nothing

            Returns
            value
        """
        return self._value

    def __eq__(self,record):
        return self._value == record.getValue()

    def __hash__(self):
        return hash(self._value)

class WordRecord(Record):
    def __init__(self,value):
        super(WordRecord,self).__init__(value.lower())

class AbilityRecord(Record):
    def __init__(self,value):
        if isinstance(value,str):
            value = value.replace("[","")
            value = value.replace("]","")
        super(AbilityRecord,self).__init__(int(value))
