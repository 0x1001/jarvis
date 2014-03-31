if __name__ == "__main__":
    from jarvis import Jarvis
    from database import WordDataBaseBuilder
    from database import TrainingDataBaseBuilder

    wd_builder = WordDataBaseBuilder()
    wd_builder.addTxtFile("learning_material/traning.txt")

    td_builder = TrainingDataBaseBuilder()
    td_builder.addTxtFile("learning_material/traning.txt")

    he = Jarvis()
    he.createWordsDataBase(wd_builder)
    he.createTrainingDataBase(td_builder)
    he.train()

    print he.respond("how are you")