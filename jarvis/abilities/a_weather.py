from ability import Ability,AbilityException

LOCATION = "Roznov pod Radhostem, CZ"

class Weather(Ability):
    def execute(self):
        """
            Weather ability. Tells weather.

            Input:
            Nothing

            Returns:
            List of word records
        """
        from database import WordRecord
        import random

        temp,wind,description = self._get_weather(LOCATION)

        response_alt1 = [WordRecord("sir"),WordRecord("it"),WordRecord("is"),WordRecord(str(temp)),WordRecord("degrees"),WordRecord("outside")]
        response_alt2 = [WordRecord("wind"),WordRecord("speed"),WordRecord("is"),WordRecord(str(wind)),WordRecord("meters"),WordRecord("per"),WordRecord("second")]
        response_alt3 = [WordRecord("sir"),WordRecord("weather"),WordRecord("description"),WordRecord("for"),WordRecord("today"),WordRecord("is")] + [WordRecord(word) for word in description.split()]

        return random.choice([response_alt1,response_alt2,response_alt3])

    def _get_weather(self,location):
        """
            Gets weather info from: http://openweathermap.org

            Input:
            Nothing

            Returns:
            temp,wind,description
        """
        import requests

        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + location

        data = self._get_url_json(url)

        temp = int(float(data["main"]["temp"]) - 272.15)
        description = str(data["weather"][0]["description"])
        wind = int(data["wind"]["speed"])

        return temp,wind,description

    def _get_url_json(self,url):
        """
            Gets json data from url

            Input:
            url     - Url

            Returns:
            json dict
        """
        import requests

        req = requests.get(url)
        try:
            return req.json()
        except ValueError:
            raise AbilityException()