from ability import Ability

class Hello(Ability):
    def execute(self):
        """
            Hello

            Input:
            Nothing

            Returns:
            List of word records
        """
        from database import WordRecord
        import datetime

        current = datetime.datetime.now()

        if current.hour > 4 and current.hour < 12:
            response = [WordRecord("good"),WordRecord("morning")]
        elif current.hour > 12 and current.hour < 18:
            response = [WordRecord("good"),WordRecord("afternoon")]
        elif ( current.hour > 18 and current.hour < 24 ) or current.hour < 4 :
            response = [WordRecord("good"),WordRecord("afternoon")]

        return response