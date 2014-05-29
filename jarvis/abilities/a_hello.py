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
        import random

        current = datetime.datetime.now()

        if current.hour >= 4 and current.hour < 12:
            response_alt1 = [WordRecord("good"),WordRecord("morning"),WordRecord("sir")]
        elif current.hour >= 12 and current.hour < 18:
            response_alt1 = [WordRecord("good"),WordRecord("afternoon"),WordRecord("sir")]
        elif ( current.hour >= 18 and current.hour <= 24 ) or current.hour < 4 :
            response_alt1 = [WordRecord("good"),WordRecord("evening"),WordRecord("sir")]

        response_alt2 = [WordRecord("hello"),WordRecord("sir")]
        response_alt3 = [WordRecord("hi"),WordRecord("sir")]

        return random.choice([response_alt1,response_alt2,response_alt3])