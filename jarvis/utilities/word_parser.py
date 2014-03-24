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

def save_list(words):
    """
        This function saves words list in file

        Input:
        words       - List of words

        Returns:
        Nothing
    """
    with open("wordslist.txt","w") as fp:
        fp.write("wordslist=[r'',\n")
        for word in words:
            fp.write("r'" + word + "',\n")
        fp.write("]\n")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='This tools parses text file and saves all words in file as array')
    parser.add_argument("-p",'--path', type=str, dest="path", help='Path to text file')

    args = parser.parse_args()

    save_list(word_parser(args.path))