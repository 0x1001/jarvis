################################################################################
################################### Class ######################################
################################################################################
class WordParseException(Exception): pass

################################################################################
################################### Functions ##################################
################################################################################

def parseContents(text):
    """
        Exctracts words from text

        Input:
        text        - Input text string

        Returns:
        list of words
    """
    import re

    if not isinstance(text,str): raise WordParseException("Not a string!")

    word_re = re.compile("[a-zA-Z]*")
    words = set()
    for word in word_re.findall(text):
            words.add(word.lower())

    return words

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
    except IOError as error: raise WordParseException(error)

def writeFileContents(path,contents):
    """
        Write contents to file path

        Input:
        path        - File path
        contents    - File contents

        Returns
        Nothing
    """
    if not isinstance(path,str): raise WordParseException("Path is not a string!")
    if not isinstance(contents,str): raise WordParseException("Contents is not a string!")

    try:
        with open(path,"w") as fp:
            fp.write(contents)
    except IOError as error: raise WordParseException(error)

def createDatabase(data_list):
    """
        Creates database from input list of string. Produces database string.
        Can be an SQL or just python list.

        Input:
        data_list       - List of string

        Returns:
        string
    """
    if not isinstance(data_list,list): raise WordParseException("Input data has to be list")

    data_string = "database=[\r'',\n"

    for element in data_list:
        if not isinstance(element,str): raise WordParseException("Input data has to be list of strings")
        data_string += "r'" + element + "',\n"

    data_string += "]\n"

    return data_string

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='This tools parses text file and saves all words in file as array')
    parser.add_argument("-p",'--path', type=str, dest="path", help='Path to text file')

    args = parser.parse_args()

    save_list(word_parser(args.path))