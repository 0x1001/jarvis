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

def run_cmd(cmd):
    """
        This function runs command

        Input:
        cmd

        Returns:
        pid
    """
    import subprocess
    return subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE).pid

def temp_path(file_name=None):
    """
        Returns path to temp dir or file

        Input:
        file_name       - File name

        Returns:
        path
    """
    import tempfile
    import os

    return tempfile.gettempdir() if file_name is None else os.path.join(tempfile.gettempdir(),file_name)

def remove(path):
    """
        Removes file/folder

        Input:
        path

        Returns:
        Nothing
    """
    import shutil
    import os

    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.unlink(path)

def is_linux():
    """
        Checks if runs on linux

        Input:
        Nothing

        Returne:
        True/False
    """
    import os

    return os.name == "posix"

def is_windows():
    """
        Checks if runs on windows

        Input:
        Nothing

        Returne:
        True/False
    """
    import os

    return os.name == "nt"
