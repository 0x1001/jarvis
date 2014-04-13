from ability import Ability

hours = ["twelve","one","two","three","four","five","six","seven","eight","nine","ten","eleven"]

class Time(Ability):
    def execute(self):
        """
            Test ability

            Input:
            Nothing

            Returns:
            List of word records
        """
        from database import WordRecord
        import datetime

        current = datetime.datetime.now()
        hours.extend(hours)

        hour = WordRecord(hours[current.hour])
        try: next_hour = WordRecord(hours[current.hour+1])
        except IndexError: next_hour = WordRecord(hours[0])

        if current.minute < 10:
            response = [WordRecord("few"),WordRecord("minutes"),WordRecord("after"),hour]
        elif current.minute < 15:
            response = [WordRecord("almost"),WordRecord("quarter"),WordRecord("past"),hour]
        elif current.minute < 20:
            response = [WordRecord("almost"),WordRecord("twenty"),WordRecord("past"),hour]
        elif current.minute < 30:
            response = [WordRecord("close"),WordRecord("to"),WordRecord("half"),WordRecord("past"),hour]
        elif current.minute < 40:
            response = [WordRecord("few"),WordRecord("minutes"),WordRecord("after"),WordRecord("half"),hour]
        elif current.minute < 45:
            response = [WordRecord("almost"),WordRecord("quarter"),WordRecord("to"),next_hour]
        elif current.minute < 50:
            response = [WordRecord("almost"),WordRecord("ten"),WordRecord("to"),next_hour]
        elif current.minute <= 59:
            response = [WordRecord("almost"),next_hour]

        return response