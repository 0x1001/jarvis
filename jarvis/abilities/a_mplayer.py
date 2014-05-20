from ability import Ability

_TEMP_FILE = "a_mplayer.pid"

class StartBBCRadio(Ability):
    def execute(self):
        """
            Start BBC Radio

            Input:
            Nothing

            Returns:
            List of word records
        """
        from database import WordRecord
        import lowlevel
        import os

        if lowlevel.is_windows():
            return [WordRecord("i"),WordRecord("am"),WordRecord("sorry"),WordRecord("sir"),WordRecord("this"),WordRecord("can"),WordRecord("run"),WordRecord("on"),WordRecord("linux"),WordRecord("only")]

        if os.path.exists(lowlevel.temp_path(_TEMP_FILE)):
            return [WordRecord("sir"),WordRecord("music"),WordRecord("is"),WordRecord("already"),WordRecord("playing")]

        pid = lowlevel.run_cmd("mplayer -playlist http://www.bbc.co.uk/worldservice/meta/live/nb/eieuk_au_nb.asx </dev/null >/dev/null 2>&1 &")

        with open(lowlevel.temp_path(_TEMP_FILE),"w") as fp:
            fp.write(str(pid))

        return [WordRecord("enjoy"),WordRecord("sir")]

class Stop(Ability):
    def execute(self):
        """
            Stops mplayer

            Input:
            Nothing

            Returns:
            Nothing
        """
	import os
        from database import WordRecord
        import lowlevel

        if lowlevel.is_windows():
            return [WordRecord("i"),WordRecord("am"),WordRecord("sorry"),WordRecord("sir"),WordRecord("this"),WordRecord("can"),WordRecord("run"),WordRecord("on"),WordRecord("linux"),WordRecord("only")]

	if not os.path.exists(lowlevel.temp_path(_TEMP_FILE)):
	    return [WordRecord("music"),WordRecord("is"),WordRecord("running"),WordRecord("sir")]

        with open(lowlevel.temp_path(_TEMP_FILE),"r") as fp:
            pid = fp.read()

        lowlevel.run_cmd("killall mplayer")

        lowlevel.remove(lowlevel.temp_path(_TEMP_FILE))

        return [WordRecord("music"),WordRecord("is"),WordRecord("stopped"),WordRecord("sir")]
