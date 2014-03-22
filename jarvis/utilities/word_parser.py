################################################################################
################################### Functions ##################################
################################################################################

def word_parser(path):
    """
        This function parses given txt file and returns list of words

        Input:
        path    - Path to file path

        Returns:
        List of words
    """
    import re

    word_re = re.compile("[a-zA-Z]*")

    with open(path,"r") as fp:
        contents = fp.readlines()

    words = set()
    for line in contents:
        for word in word_re.findall(line):
            words.add(word.lower())

    return list(words)

def save_list(words):
    """
        This function saves words list in file

        Input:
        words       - List of words

        Returns:
        Nothing
    """
    with open("wordslist.txt","w") as fp:
        fp.write("wordslist=[\n")
        for word in words:
            fp.write("r'" + word + "',\n")
        fp.write("]\n")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='This tools parses text file and saves all words in file as array')
    parser.add_argument("-p",'--path', type=str, dest="path", help='Path to text file')

    args = parser.parse_args()

    save_list(word_parser(args.path))