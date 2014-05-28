from ability import Ability,AbilityException

class MediaCenter(object):
    """
        Media Center for controling mplayer
        Linux only

        Attributes:
        _player     - Player instance
    """
    def __init__(self):
        import lowlevel

        if lowlevel.is_linux():
            try:
                import mplayer
            except ImportError:
                raise AbilityException("mplayer.py is not installed!")

            self._player = mplayer.Player()
        else:
            self._player = None

    def factoryBBCRadioStart(self):
        """
            Creates ability BBCRadioStart

            Input:
            Nothing

            Returns:
            Nothing
        """
        ability = BBCRadioStart()
        ability.player(self._player)

        return ability

    def factoryStop(self):
        """
            Creates ability Stop

            Input:
            Nothing

            Returns:
            Nothing
        """
        ability = Stop()
        ability.player(self._player)

        return ability

class MediaCenterAbility(Ability):
    def __init__(self):
        super(MediaCenterAbility,self).__init__()
        self._player = None

    def player(self,player):
        """
            This method sets player

            Input:
            player  - Player

            Returns:
            Nothing
        """
        self._player = player

    def _check_player(self):
        """
            Checks if player is set

            Input:
            Nothing

            Returns:
            True/False
        """
        return not self._player is None

class BBCRadioStart(MediaCenterAbility):
    def execute(self):
        from database import WordRecord

        if not self._check_player():
            return [WordRecord("sir"),WordRecord("i"),WordRecord("cannot"),WordRecord("find"),WordRecord("music"),WordRecord("player")]

        self._player.loadlist("http://www.bbc.co.uk/worldservice/meta/live/nb/eieuk_au_nb.asx")

        return [WordRecord("enjoy"),WordRecord("sir")]

class Stop(MediaCenterAbility):
    def execute(self):
        from database import WordRecord

        if not self._check_player():
            return [WordRecord("sir"),WordRecord("i"),WordRecord("cannot"),WordRecord("find"),WordRecord("music"),WordRecord("player")]

        self._player.stop()

        return [WordRecord("music"),WordRecord("is"),WordRecord("stopped"),WordRecord("sir")]