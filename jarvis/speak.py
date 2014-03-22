################################################################################
################################### Class ######################################
################################################################################
class SpeakError(Exception): pass

################################################################################
################################### Function ###################################
################################################################################

def sentenceToNumbers(sentence):
    """
        Converts sentence to numbers

        Input:
        sentence    - list of words

        Returns:
        List of numbers
    """
    import database

    numbers_list = []
    for word in sentence:
        try: numbers_list.append(database.wordToNumber(word))
        except database.DataBaseError: raise SpeakError("Cannot find '" + word + "' in database!")

    return numbers_list

def numbersToSentence(numbers):
    """
        This function convertes list of numbers to sentence

        Input:
        numbers     - List of numbers

        Returns:
        sentence
    """
    import database

    sentence = []
    for num in numbers:
        try: sentence.append(database.numbertToWord(num))
        except database.DataBaseError: raise SpeakError("Cannot find word for index: '" + str(num) + "' in database!")

    return sentence
