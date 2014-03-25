class LowLevelException(Exception): pass

def readFileContents(path):
    """
        Reads file contents

        Input:
        Path        - Path to file

        Retruns:
        File contents
    """
    try:
        with open(path,"r") as fp:
            return fp.read()
    except IOError as error: raise LowLevelException(error)

def writeFileContents(path,contents):
    """
        Write contents to file path

        Input:
        path        - File path
        contents    - File contents

        Returns
        Nothing
    """
    if not isinstance(path,str): raise LowLevelException("Path is not a string!")
    if not isinstance(contents,str): raise LowLevelException("Contents is not a string!")

    try:
        with open(path,"w") as fp:
            fp.write(contents)
    except IOError as error: raise LowLevelException(error)